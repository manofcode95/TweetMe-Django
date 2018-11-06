from tweets_app.models import Tweet
from account_app.api.serializers import UserDefaultSerializer
from rest_framework import serializers
from django.utils.timesince import timesince
from django.urls import reverse_lazy

class ParentTweetModelSerializer(serializers.ModelSerializer):
    author=UserDefaultSerializer(read_only=True)
    time_display=serializers.SerializerMethodField()
    author_url=serializers.SerializerMethodField()
    content_url=serializers.SerializerMethodField()
    retweet_url= serializers.SerializerMethodField()
    class Meta:
        model=Tweet
        fields=['author', 'pk', 'content', 'time_display', 'author_url', 'content_url',  'retweet_url']

    def get_time_display(self, obj):
        date_display= obj.created_date.strftime("%d %B")
        time_since= timesince(obj.created_date) +' ago'
        if 'day' not in time_since and 'month'not in time_since and 'year' not in time_since:
            return time_since
        else:
            return date_display

    def get_author_url(self, obj):
        return reverse_lazy('profile_app:user_detail', kwargs={'username':obj.author})
    
    def get_content_url(self,obj):
        return obj.get_absolute_url()

    def get_retweet_url(self, obj):
        return reverse_lazy('api_tweet:api_retweet', kwargs={'pk':obj.pk}) 

class TweetModelSerializer(serializers.ModelSerializer):
    author=UserDefaultSerializer(read_only=True)
    time_display=serializers.SerializerMethodField()
    author_url=serializers.SerializerMethodField()
    content_url=serializers.SerializerMethodField()
    parent=ParentTweetModelSerializer(read_only=True)
    retweet_url= serializers.SerializerMethodField()
    
    class Meta:
        model=Tweet
        fields=['author','content', 'time_display', 'author_url', 'content_url', 'parent', 'pk', 'retweet_url']

    def get_time_display(self, obj):
        date_display= obj.created_date.strftime("%d %B")
        time_since= timesince(obj.created_date) +' ago'
        if 'day' not in time_since and 'month'not in time_since and 'year' not in time_since:
            return time_since
        else:
            return date_display

    def get_author_url(self, obj):
        return reverse_lazy('profile_app:user_detail', kwargs={'username':obj.author})
    
    def get_content_url(self,obj):
        return obj.get_absolute_url()
    
    def get_retweet_url(self, obj):
        return reverse_lazy('api_tweet:api_retweet', kwargs={'pk':obj.pk}) 