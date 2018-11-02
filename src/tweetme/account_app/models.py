from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class UserProfileManager(models.Manager):
    def all(self):
        qs=self.get_queryset().all()
        if self.instance:
            qs=qs.exclude(user=self.instance)
        return qs

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    following=models.ManyToManyField(User, blank=True, null=True, related_name='followed_by')
    objects=UserProfileManager()
    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        qs=self.following.exclude(username=self.user)
        return qs
    
