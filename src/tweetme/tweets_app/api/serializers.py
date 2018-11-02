from tweets_app.models import Tweet
from account_app.api.serializers import UserDefaultSerializer
from rest_framework import serializers
from django.utils.timesince import timesince
from django.urls import reverse_lazy
class TweetModelSerializer(serializers.ModelSerializer):
    author=UserDefaultSerializer(read_only=True)
    time_display=serializers.SerializerMethodField()
    url=serializers.SerializerMethodField()
    class Meta:
        model=Tweet
        fields=['author','content', 'time_display', 'url']

    def get_time_display(self, obj):
        date_display= obj.created_date.strftime("%d %B")
        time_since= timesince(obj.created_date) +' ago'
        if 'day' not in time_since and 'month'not in time_since and 'year' not in time_since:
            return time_since
        else:
            return date_display

    def get_url(self, obj):
        return reverse_lazy('profile_app:user_detail', kwargs={'username':obj.author})