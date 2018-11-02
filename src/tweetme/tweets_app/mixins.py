from django.shortcuts import redirect
from django.core.exceptions import ValidationError, PermissionDenied
from django.http import HttpResponseForbidden, HttpResponseRedirect

class FormUserNeededMixin():
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author=self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        form.add_error(field=None, error='You must log in to continue')
        return self.form_invalid(form)

class FormUserOwnerMixin(object):
    def form_valid(self, form):
        if form.instance.author==self.request.user:      
            return super(FormUserOwnerMixin, self).form_valid(form)
        form.add_error(field=None, error='This user is not allowed')
        return self.form_invalid(form)


class DeleteUserOwnerMixin(object):
    def post(self, request, *args, **kwargs):
        if self.get_object().author==self.request.user:
            return super(DeleteUserOwnerMixin, self).post(request, args, kwargs)
        # raise PermissionDenied
        return HttpResponseForbidden("403 Forbidden , you don't have access")

class AuthRequiredMixin(object):
     def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('/admin/')
        return super(AuthRequiredMixin, self).dispatch(
            request, *args, **kwargs)