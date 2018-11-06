from django.conf.urls import url
from .views import TweetListAPIView, TweetCreateAPIView, RetweetAPIView, LikeToggleAPIView

app_name='api_tweet'

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='api_list'), # /api/tweet/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='api_create'),
    url(r'^(?P<pk>[\d-]+)/retweet/$', RetweetAPIView.as_view(), name='api_retweet'),
    url(r'^(?P<pk>[\d-]+)/like/$', LikeToggleAPIView.as_view(), name='like_toggle'),
]

