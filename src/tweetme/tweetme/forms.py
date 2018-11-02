from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class LoginForm(forms.Form):
    username=forms.CharField(max_length=24)
    password=forms.CharField(max_length=24, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=24)
    email=forms.EmailField()
    password=forms.CharField(max_length=24, widget=forms.PasswordInput())

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs= User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Please choose other username')
        return username