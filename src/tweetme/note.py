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

19. You can use HttpResponseRedirect or redirect to redirect url
url=reverse_lazy('profile_app:user_detail', kwargs={'username':username})
HttpResponseRedirect(url)
or
redirect(reverse_lazy('profile_app:user_detail', kwargs={'username':username}))
or
redirect('profile_app:user_detail', username=username)

20. user_profile, created= UserProfile.objects.get_or_create(user=request.user)
created==True means object had not been created unitl now.
created==False means objects has already been created.

21. create self object from models.manager: obj=self.model(field=value...)->obj.save()
or you can use <Model>.objects.create

22. 2 models cannot import each other-->
from tweet.models import hashtag
from hastag.models import tweet

23. This is how signal works:
if you want to create tag page everytime after posting a tweet:
    #  create signal to get the information you want

    hashtags_app.signal: parsed_hashtags=Signal(providing_args=['hashtag_list']) 

    #  connect receiver function: it will get that signal and handel it
    def parsed_hashtags_receiver(sender, hashtag_list, *args, **kwargs):
    if len(hashtag_list)>=1:
        for tag in hashtag_list:
            HashTag.objects.get_or_create(tag=tag)

    parsed_hashtags.connect(parsed_hashtags_receiver)

    # connect to signals sent. Everytime run the signal, they know where to send to
    def tweet_save_receiver(sender, instance, created, **kwargs):
    if created and not instance.parent:

        hash_regex=r'#(?P<hashtag>[\w]+)'
        hashtags=re.findall(hash_regex,content)
        parsed_hashtags.send(sender=instance.__class__, hashtag_list= hashtags )

    post_save.connect(tweet_save_receiver, sender=Tweet)


23. In Jquery: 
$(".btn-like").on(...)
var this_ = $(this): will only change that specific class
$(".btn-like").fucntion: will change all the values in that class

24. To pass context from Views to Serializer:
in Views:
   def get_serializer_context(self, *args, **kwargs):
        context=super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request']=self.request
        return context

In Serializer:
    def get_did_like(self, obj):
        request=self.context.get('request')
        user=request.user

25. not really understand about parent_id. Check it later.
26. Get the query "q" from request.GET not kwargs