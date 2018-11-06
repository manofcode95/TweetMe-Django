from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.db.models.signals import post_save
User = get_user_model()
# Create your models here.
class UserProfileManager(models.Manager):
    def all(self):
        qs=self.get_queryset().all()
        if self.instance:
            qs=qs.exclude(user=self.instance)
        return qs

    def toggle_follow(self, user,toggle_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if toggle_user in user_profile.following.all():
            user_profile.following.remove(toggle_user)
            added=False
        else:
            user_profile.following.add(toggle_user)
            added=True
        return added

    def is_following(self, user, toggle_user):
        user_profile, created= UserProfile.objects.get_or_create(user=user)
        if toggle_user in user_profile.following.all():
            return True
        return False

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    following=models.ManyToManyField(User, blank=True, related_name='followed_by')
    objects=UserProfileManager()
    def __str__(self):
        # return str(self.following.all().count())
        return self.user.username

    def get_following(self):
        qs=self.following.exclude(username=self.user)
        return qs
    
    def get_follow_url(self):
        return reverse_lazy('profile_app:user_follow', kwargs={'username':self.user.username})

    def get_absolute_url(self):
        return reverse_lazy('profile_app:user_detail', kwargs={'username':self.user.username})

def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
post_save.connect(post_save_user_receiver, sender=User)