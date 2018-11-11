from django.db import models
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from . import validate
import re
from django.db.models.signals import post_save
from hashtags_app.signals import parsed_hashtags
# from hashtags_app.models import HashTag
# Create your models here.
class TweetManager(models.Manager):
    def retweet(self, retweet_user, parent_obj):
        if parent_obj.parent:
            og_parent=parent_obj.parent
        else:
            og_parent=parent_obj
        qs=self.get_queryset().filter(author=retweet_user, parent=og_parent)
        if qs.exists():
            return None
        obj=self.model(parent=og_parent,
                       author=retweet_user,
                       content=parent_obj.content)
        obj.save()
        return obj

        
    def like_toggle(self, user, tweet_obj):
        if user in tweet_obj.like.all():
            like=False
            tweet_obj.like.remove(user)
        else:
            like=True
            tweet_obj.like.add(user)
        return like
class Tweet(models.Model):
    parent=models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    content = models.TextField(max_length=140, validators=[validate.validate_content])
    like=models.ManyToManyField(get_user_model(), blank=True, related_name='liked')
    reply = models.BooleanField(verbose_name="Is this a reply", default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    objects=TweetManager()

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self,*args,**kwargs):
        return reverse('tweet_app:tweet_detail', kwargs={"pk":self.pk})
    
    def is_retweet(self):
        if self.parent:
            return True
        return False
    def get_parent(self):
        the_parent=self
        if self.parent:
            the_parent=self.parent
        return the_parent

    def get_children(self):
        parent=self.get_parent()
        children_obj = Tweet.objects.filter(parent=parent)  
        parent_obj = Tweet.objects.filter(pk=parent.pk)  
        qs = (children_obj|parent_obj).distinct().order_by('pk')
        return qs

    class Meta:
        ordering=['-id']

def tweet_save_receiver(sender, instance, created, **kwargs):
    if created and not instance.parent:
        user_regex=r'@(?P<username>[\w]+)'
        content=instance.content
        usernames=re.findall(user_regex,content)

        hash_regex=r'#(?P<hashtag>[\w]+)'
        hashtags=re.findall(hash_regex,content)
post_save.connect(tweet_save_receiver, sender=Tweet)