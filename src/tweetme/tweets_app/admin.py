from django.contrib import admin
from .models import Tweet
from .forms import TweetForm
# Register your models here.

# class TweetFormAdmin(admin.ModelAdmin):
#     form=TweetForm
    

# admin.site.register(Tweet, TweetFormAdmin)
admin.site.register(Tweet)