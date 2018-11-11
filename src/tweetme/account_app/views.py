from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import UserProfile
User=get_user_model()
# Create your views here.
class UserDetailView(DetailView):
    queryset=User.objects.all()
    template_name='accounts/user_detail.html'
    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, username__iexact=self.kwargs.get('username'))

    def get_context_data(self, *args, **kwargs):
        context=super(UserDetailView, self).get_context_data()
        context['is_following']=UserProfile.objects.is_following(self.request.user, self.get_object(*args, **kwargs))
        context['recommended']=UserProfile.objects.recommended(self.request.user,3)
        return context

class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):  
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect('profile_app:user_detail', username=username)
