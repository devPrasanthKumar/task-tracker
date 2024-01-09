from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("createaccount/", views.UserRegisterView.as_view(), name="create-account"),
    path("", views.UserLoginView.as_view(), name="user-login"),
    path("logout/", LogoutView.as_view(), name="user-logout"),
]
