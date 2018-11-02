from .models import Tweet
from django import forms

class TweetForm(forms.ModelForm):
    content=forms.CharField(label='', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'Enter message'}))
    class Meta:
        model=Tweet
        fields=['content']
