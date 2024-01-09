from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render, resolve_url

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse

from .forms import AccountCreateForm
from taskTrackingApp.models import UserProfileModel

from django.contrib.auth.mixins import LoginRequiredMixin

# creating user account


class UserRegisterView(CreateView):
    form_class = AccountCreateForm
    template_name = "auth/create_account_form.html"
    success_url = reverse_lazy("user-login")


# implemented login
class UserLoginView(LoginView):
    template_name = "auth/user_login_form.html"

    # after logged in
    def get_success_url(self):
        user_profile = UserProfileModel.objects.get(user=self.request.user)
        return reverse("user-detail", kwargs={'pk': user_profile.pk})

    ''' 
    if user already logged in and they wants to revist this page(https://127.0.0.1/home) after exit from the site..
    they will automatically redirect to the home page otherwise they should login 
    '''

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)


# logout
class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('user-login')
    login_url = reverse_lazy("user-login")
