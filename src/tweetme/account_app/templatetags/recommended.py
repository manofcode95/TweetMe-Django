from django import template
from django.contrib.auth import get_user_model
from account_app.models import UserProfile
User=get_user_model()


register = template.Library()


@register.inclusion_tag('accounts/snippets/recommended.html')
def recommended(user):
    if isinstance(user, User):
        qs=UserProfile.objects.recommended(user, 3)
        return {'object_list':qs}