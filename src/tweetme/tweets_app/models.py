from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from . import validate
# Create your models here.

class Tweet(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    content = models.TextField(max_length=140, validators=[validate.validate_content])
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self,*args,**kwargs):
        return reverse('tweet_app:tweet_detail', kwargs={"pk":self.pk})
    
    class Meta:
        ordering=['-id']
