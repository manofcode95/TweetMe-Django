from django.conf import settings
from django.conf.urls import url, include
from .views import TweetList, TweetDetail, TweetCreate, TweetUpdate, TweetDelete, Retweet

app_name='tweet_app'

urlpatterns = [
    url(r'^list/$', TweetList.as_view(), name='tweet_list'),
    url(r'^(?P<pk>\d+)/$', TweetDetail.as_view(), name='tweet_detail'),
    url(r'create/$', TweetCreate.as_view(), name='tweet_create'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdate.as_view(), name='tweet_update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDelete.as_view(), name='tweet_delete'),
    url(r'^(?P<pk>\d+)/retweet/$', Retweet.as_view(), name='retweet'),
    
]