from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.views.generic import ListView
from django.views.generic.edit import FormView
User=get_user_model()

class RegisterView(FormView):
    template_name='registration/register.html'
    form_class=RegisterForm
    success_url='/accounts/login/'
    def form_valid(self, form):
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=User.objects.create_user(username=username, email=email, password=password)
        return super(RegisterView,self).form_valid(form)


class SearchView(ListView):
    template_name="search.html"
    
    def get_queryset(self):
        query=self.request.GET.get('q')
        qs=None
        if query:
            qs=User.objects.filter(username=query)
        return qs
    def get_context_data(self, *args, **kwargs):
        context=super(SearchView, self).get_context_data(*args, **kwargs)
        return context