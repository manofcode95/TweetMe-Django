from django.conf.urls import url
from .views import UserDetailView

app_name='profile_app'
urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', UserDetailView.as_view(), name='user_detail'), # /api/tweet/
]

