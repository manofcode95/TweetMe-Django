from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Tweet
from .forms import TweetForm
from .mixins import FormUserNeededMixin, FormUserOwnerMixin, DeleteUserOwnerMixin, AuthRequiredMixin

# Create your views here.
class Retweet(View):
    def get(self, request, pk, *args, **kwargs):
        tweet=get_object_or_404(Tweet, pk=pk)
        print(tweet)
        if request.user.is_authenticated():
            new_tweet=Tweet.objects.retweet(request.user, tweet)
            print(new_tweet)
            # return redirect(new_tweet.get_absolute_url())
            return redirect('/')
        return redirect(tweet.get_absolute_url())

class TweetList(LoginRequiredMixin, ListView):
    paginate_by=5
    #  Search
    def get_queryset(self,*args,**kwargs): 
        qs=Tweet.objects.all()
        query=self.request.GET.get('q', None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query)|
                Q(author__username__icontains=query))
            return qs
        return qs   
    def get_context_data(self,**kwargs):
        context=super(TweetList,self).get_context_data(**kwargs)
        context['form']=TweetForm
        context['form_url']=reverse_lazy('tweet_app:tweet_create')
        return context

class TweetDetail(DetailView):
    queryset=Tweet.objects.all()

class TweetCreate(FormUserNeededMixin, CreateView):
    template_name='tweets_app/tweet_form.html'
    form_class=TweetForm
    

class TweetUpdate(LoginRequiredMixin, FormUserOwnerMixin, UpdateView):
    model=Tweet
    form_class=TweetForm
    template_name='tweets_app/tweet_form.html'
    redirect_field_name=reverse_lazy('tweet_app:tweet_list')
    


class TweetDelete(DeleteUserOwnerMixin, DeleteView):
    model=Tweet
    success_url=reverse_lazy('tweet_app:tweet_list')
    

def home1(request):
    print(request.user)
    return render(request, 'home.html',{})















#------------CreateView by function-------------------# 
# def tweet_create_view(request):
#     form=TweetForm(request.POST or None)
#     if form.is_valid():
#         instance=form.save(commit=False)
#         instance.author=request.user
#         instance.save()
#     context={'form':form}
#     return render(request, 'tweets_app/tweet_form.html', context)