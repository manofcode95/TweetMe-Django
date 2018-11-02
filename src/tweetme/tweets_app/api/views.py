from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from tweets_app.models import Tweet

from .pagination import StandardResultsPagination
from .serializers import TweetModelSerializer


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    queryset=Tweet.objects.all()
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TweetListAPIView(generics.ListAPIView):
    serializer_class=TweetModelSerializer
    pagination_class=StandardResultsPagination
    def get_queryset(self,*args,**kwargs):
        qs=Tweet.objects.all()
        query=self.request.GET.get('q', None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query)|
                Q(author__username__icontains=query))
            return qs
        return qs  


    


    
