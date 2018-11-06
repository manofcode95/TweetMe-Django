from django.conf.urls import url
from tweets_app.api.views import TweetListAPIView

app_name='account_api'
urlpatterns = [
    url(r'^(?P<username>[\w-]+)/tweet/$', TweetListAPIView.as_view(), name='user_api'),
]

