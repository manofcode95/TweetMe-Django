# from django.db import models
# from tweets_app.models import Tweet
# from django.contrib.auth import get_user_model
# User=get_user_model()


# # Create your models here.
# class Reply(models.Model):
#     tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     content= models.CharField(max_length=150)