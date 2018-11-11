"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from tweets_app import views
from .views import RegisterView, SearchView
from hashtags_app.views import HashTagView
from hashtags_app.api.views import HashTagAPIView
urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', views.TweetList.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    # tweets_app
    url(r'^tweet/', include('tweets_app.urls')),
    url(r'^api/tweet/', include('tweets_app.api.urls', namespace='tweet-api')),
    #search
    url(r'^search/$', SearchView.as_view(), name='search'),
    # account_app
    url(r'^profile/', include('account_app.urls')),
    url(r'^api/', include('account_app.api.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # hashtags_app
    url(r'^tags/(?P<hashtag>[\w-]+)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^api/tags/(?P<hashtag>[\w-]+)/$', HashTagAPIView.as_view(), name='hashtag'),
    # login,logout,register
    url(r'^accounts/register/$', RegisterView.as_view(), name='register'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)