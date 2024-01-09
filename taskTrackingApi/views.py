
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
# models
from taskTrackingApp.models import AndroidAppModel,  TaskModel, UserProfileModel
from django.db.models import Sum

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# views
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView,  RetrieveUpdateAPIView
from rest_framework.mixins import RetrieveModelMixin
# serialziers
from .serializers import AndroidAppSerializer,  TaskSerializer, UserPointSerializer
from taskTrackingApiAuth.serializer import UserProfileSerializer

# permissions
from .custom_permissions import AdminCanAccess


class CreateAndroidAppView(ModelViewSet):

    ''' 
    this 'AddAndroidAppview' helps to create a post, admin can only post the data 
    because i have added the custom authentication.
    '''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAccess]
    queryset = AndroidAppModel.objects.all()
    serializer_class = AndroidAppSerializer

    # the data saves belongs to the user(current user)
    def perform_create(self, serializer):
        get_user = get_object_or_404(
            UserProfileModel, pk=self.request.user.userprofile.pk)
        serializer.save(user=get_user)


# Normal User Section
class ShowAppsForUserView(ListAPIView, RetrieveModelMixin):

    '''
    normal user can see all details about the apps.
    but they can't modify anything on apps which is made by admin user
    '''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = AndroidAppModel.objects.all()
    serializer_class = AndroidAppSerializer
    lookup_field = "pk"

    ''' 
    here , i override the list action ,if user makes a request for retrieve particular data by 'pk' it will show a app ,
    otherwise it will show all apps 
    '''

    def list(self, request, *args, **kwargs):
        if self.lookup_field in kwargs:
            return super().retrieve(request, *args, **kwargs)
        else:
            return super().list(request, *args, **kwargs)


class UserTaskView(ListCreateAPIView):

    ''' 
    normal_user can upload their task for the specific app by the app's id 
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()

    def perform_create(self, serializer):
        get_id = self.kwargs.get("pk")
        get_post = get_object_or_404(AndroidAppModel, pk=get_id)
        get_user = get_object_or_404(
            UserProfileModel, pk=self.request.user.userprofile.pk)
        serializer.save(user=get_user, app=get_post)
        return super().perform_create(serializer)

    def create(self, request, *args, **kwargs):
        return Response({"message": "Task created successfully"}, status=status.HTTP_201_CREATED)


# it shows the user's points
class UserPointsView(ListAPIView):

    serializer_class = UserPointSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # it will calculate the points
        total_points = AndroidAppModel.objects.aggregate(
            points_sum=Sum("points"))["points_sum"]
        return [{"points": total_points}]


class UserProfileView(RetrieveUpdateAPIView):

    ''' 
    normal_users can see their details,
    they can  see  only their details , they can't  allow to see other's detail
    '''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    queryset = UserProfileModel.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
