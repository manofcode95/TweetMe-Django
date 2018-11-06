from django.conf.urls import url
from .views import UserDetailView, UserFollowView

app_name='profile_app'
urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^(?P<username>[\w-]+)/follow/$', UserFollowView.as_view(), name='user_follow'),
]

