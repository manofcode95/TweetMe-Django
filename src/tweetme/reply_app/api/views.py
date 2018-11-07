# from rest_framework.generics import CreateAPIView
# from rest_framework import permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import ReplySerializer

# from reply_app.models import Reply
# from tweets_app.models import Tweet
# class CreateReplyAPIView(CreateAPIView):
#     print(11)
#     permission_classes=permission_classes=[permissions.IsAuthenticatedOrReadOnly]
#     serializer_class=ReplySerializer
#     queryset=Reply.objects.all()

#     def perform_create(self, pk, serializer):
#         tweet=Tweet.objects.filter(pk=pk)
#         if tweet.exist():
#             serializer.save(user=self.request.user, tweet=tweet)
    