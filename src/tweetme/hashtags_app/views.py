from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import HashTag
# Create your views here.
class HashTagView(View):
    def get(self, request, hashtag, *args,**kwargs):
        hash_tag, created = HashTag.objects.get_or_create(tag=hashtag)
        return render(self.request, 'hashtags_app/view.html', {'object':hash_tag})
