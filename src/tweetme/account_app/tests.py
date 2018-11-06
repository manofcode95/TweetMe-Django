from django.test import TestCase
from .models import UserProfile
from django.contrib.auth import get_user_model

# Create your tests here.
User= get_user_model()

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.username="some_user"
        User.objects.create(username=self.username)
    
    def test_create_user_profile(self):
        user_profile=UserProfile.objects.filter(user__username=self.username)
        self.assertTrue(user_profile.count()==1)
    
    def test_create_same_user(self):
        User.objects.create(username=self.username+'a')