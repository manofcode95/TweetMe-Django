from django.conf.urls import url
from .views import TweetListAPIView, TweetCreateAPIView, RetweetAPIView, LikeToggleAPIView, TweetRetrieveAPIView, SearchAPIView

app_name='api_tweet'

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='api_list'), # /api/tweet/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='api_create'),
    url(r'^search/$', SearchAPIView.as_view(), name='api_search'),
    url(r'^(?P<pk>[\d]+)/$', TweetRetrieveAPIView.as_view(), name='api_detail'),
    url(r'^(?P<pk>[\d]+)/retweet/$', RetweetAPIView.as_view(), name='api_retweet'),
    url(r'^(?P<pk>[\d]+)/like/$', LikeToggleAPIView.as_view(), name='like_toggle'),
]

