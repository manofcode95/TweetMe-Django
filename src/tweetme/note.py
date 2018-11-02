1. #Don't forget the brackets [] 
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static-storage")]

2. #There are 3 ways to import User
+ User
+ AUTH_USER_MODEL
+ get_user_model()
https://wsvincent.com/django-referencing-the-user-model/
#The best choice is always get_user_model() (from django.contrib.auth import get_user_model)

3.
class TweetDetail(DetailView):
    queryset=Tweet.objects.all()
    def get_context_data(self,*args,**kwargs):
        object=super(TweetDetail,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        print(pk)
        return object
To get the pk, run pk=self.kwargs.get('pk') not pk=self.kwargs['pk'](may causes some errors)

4. Some sorts of Validation for forms:
+ Cleaning a specific field attribute: def clean_<field_name>(self):
+ Cleaning and validating fields that depend on each other: def clean(self):
But you have to copy and paste if you want to reuse again!
+ The best way is to use validator built-in.
Create a new python file validators.py to write validate code.
https://docs.djangoproject.com/en/2.1/ref/validators/
5. When use CRUDView, use rediect and reverse_lazy to redirect. "reverse" may causes errors.
6. To auto add the value for a field, use form_valid:
def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-editing/
form.instance.<name_field>=value
7. You can create LoginMixin yourselve (can see the view function and show errors) or using LoginRequiredMixin(cant see the view and redirect to login page)
8. Refer this tutorial to make pagination:
https://docs.djangoproject.com/en/2.1/ref/class-based-views/mixins-multiple-object/
https://docs.djangoproject.com/en/2.1/topics/pagination/
9. Use django.db.models.Q for the look up.
If you look up for user, refer these commands:
def get_queryset(self,*args,**kwargs):
        qs=Tweet.objects.all()
        print(self.request.GET)
        query=self.request.GET .get('q', None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query)|
                Q(author__username__icontains=query))### no idea what __username is
            return qs
        return qs
https://docs.djangoproject.com/en/2.1/topics/db/queries/
10. If you want to get the content of the block from the parent template, {{ block.super }} variable will do the trick.
11. Create pagination:
https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
12. for ... empty ... endfor
Loop the code from for...empty
13. Install Pillow==3.1
pip install --upgrade pillow --global-option="build_ext" --global-option="--disable-jpeg" --global-option="--disable-zlib"

14. Some useful exceptions: https://docs.djangoproject.com/en/2.1/ref/exceptions/
from django.http import HttpResponseForbidden
return HttpResponseForbidden("403 Forbidden , you don't have access")

15. There're several ways to change the orders of the objects.
+ in object model:
class Meta:
    ordering=['id']
+ ObjectModel.objects.all().order_by('-id')
+ In the manager model, edit the alL() function

16. Change the date display:
http://strftime.org/
obj_date.strftime("%d %B")

17. self.field.all()
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    following=models.ManyToManyField(User, blank=True, null=True, related_name='followed_by')

    def __str__(self):
        return str(self.following.all())
18. don't know what it's able to call .count function
Followed By ({{object.followed_by.all.count}})