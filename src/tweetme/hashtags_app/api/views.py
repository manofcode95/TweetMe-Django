
from rest_framework import generics
from tweets_app.api.pagination import StandardResultsPagination
from tweets_app.api.serializers import TweetModelSerializer
from tweets_app.models import Tweet
from hashtags_app.models import HashTag
class HashTagAPIView(generics.ListAPIView):
    serializer_class=TweetModelSerializer
    pagination_class=StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context=super(HashTagAPIView, self).get_serializer_context(*args, **kwargs)
        context['currentuser']=self.request.user
        return context

    def get_queryset(self,*args,**kwargs):
        hashtag=self.kwargs.get('hashtag')
        hashtag_obj = None
        try:
            hashtag_obj = HashTag.objects.get_or_create(tag=hashtag)[0]
        except:
            pass
        if hashtag_obj:
            qs=hashtag_obj.get_tweets()
        else:
            qs=None

        query=self.request.GET.get('q',None)
        if query:
            qs=qs.filter(Q(author__username=query)| Q(content__icontains=query))
            print('yes')
        return qs  
