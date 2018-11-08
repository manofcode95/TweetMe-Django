from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .pagination import StandardResultsPagination
from .serializers import TweetModelSerializer

from tweets_app.models import Tweet
from account_app.models import UserProfile

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
User=get_user_model()


class LikeToggleAPIView(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk, format=None):
        tweet_obj=get_object_or_404(Tweet, pk=pk)
        if tweet_obj:
            is_liked=Tweet.objects.like_toggle(request.user, tweet_obj)
            if is_liked:
                likebtn='Unlike'
            else:
                likebtn='Like'
            return Response({'liked':is_liked, 'likebtn':likebtn})
        return Response(None, status=400)

class RetweetAPIView(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk, format=None):
        tweet_qs=Tweet.objects.filter(pk=pk)
        retweeted = Tweet.objects.filter(author=request.user, pk=tweet_qs.first().pk)
        if tweet_qs.exists() and not retweeted.exists():
            new_tweet=Tweet.objects.retweet(retweet_user=request.user, parent_obj=tweet_qs.first())
            data=TweetModelSerializer(new_tweet).data
            return Response(data)
        return Response(None, status=400)
        
class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    queryset=Tweet.objects.all()
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TweetRetrieveAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class=StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        tweet_id=self.kwargs.get('pk')
        qs=Tweet.objects.filter(pk=tweet_id)
        return qs

class TweetListAPIView(generics.ListAPIView):
    serializer_class=TweetModelSerializer
    pagination_class=StandardResultsPagination
    def get_queryset(self,*args,**kwargs):
        request_username=self.kwargs.get('username')
        if request_username:
            qs=Tweet.objects.filter(author__username=request_username)
        else:
            im_following=self.request.user.profile.following.all()
            my_user=User.objects.get(username=self.request.user.username)
            qs=Tweet.objects.filter(Q(author__in=im_following)|Q(author=my_user))

        query=self.request.GET.get('q', None)    
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query)|
                Q(author__username__icontains=query))
            return qs
        return qs  


    def get_serializer_context(self, *args, **kwargs):
        context=super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context['currentuser']=self.request.user
        return context


    
