from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register("addapp", views.CreateAndroidAppView, basename="add-app")

urlpatterns = [
    path("", include(router.urls)),
    path("showappsforuser/", views.ShowAppsForUserView.as_view(),
         name="show-details"),
    path("showappsforuser/<int:pk>", views.ShowAppsForUserView.as_view(),
         name="show-details"),
    path("task/<int:pk>",
         views.UserTaskView.as_view(), name="task"),
    path("userpoints/", views.UserPointsView.as_view(), name="user-points"),
    path("showuserprofile/<uuid:pk>",
         views.UserProfileView.as_view(), name="show-user-profile"),

    # swagger for api documentation
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

]
