from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("userprofile/<uuid:pk>",
         views.UserProfileView.as_view(), name="user-detail"),
    path("singledata/<int:pk>", views.ShowSingleAppView.as_view(), name="single-app"),
    path("updateprofile/<uuid:pk>",
         views.UpdateUserProfileView.as_view(), name="update-user"),
    path("showcompletedtask/",
         views.ShowCompletedTaskView.as_view(), name="show-completed-task"),
    path("showpoints/", views.ShowPointsView.as_view(), name="show-points"),


]
