from django.urls import path

# importing our views
from .views import UserLoginView, UserLogoutView, UserAcountCreateView

app_name = "auth"

urlpatterns = [
    path("register/", UserAcountCreateView.as_view(), name="create-account"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("logout/", UserLogoutView.as_view(), name="user-logout"),
]
