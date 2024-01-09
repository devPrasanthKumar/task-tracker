from django.db import models

from django.db import models
from taskTrackingAuthApp.models import User
from django.contrib.auth import get_user_model
import uuid

# model for adding a app details by admin_user


class UserProfileModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="userprofile")
    username = models.CharField(max_length=300)
    user_email = models.EmailField(max_length=100)
    user_points = models.IntegerField(null=True, blank=True)
    # implemented uuid for user for security purpose,it will be considered as pk
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.username


class AndroidAppModel(models.Model):
    APP_CATEGORY = [
        ("Entertainment", "Entertainment"),
        ("Education", "Education"),
        ("Lifestyle", "Lifestyle")
    ]

    APP_SUB_CATEGORY = [
        ("Social Media", "Social Media"),
        ("Blog", "Blog"),
        ("Live Streaming", "Live Streaming")
    ]

    user = models.ForeignKey(
        UserProfileModel, on_delete=models.CASCADE, related_name="app_username")
    app_name = models.CharField(max_length=400)
    app_link = models.URLField(max_length=1000)
    app_category = models.CharField(max_length=100, choices=APP_CATEGORY)
    app_sub_category = models.CharField(
        max_length=100, choices=APP_SUB_CATEGORY)
    points = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.app_name


class TaskModel(models.Model):
    user = models.ForeignKey(
        UserProfileModel, on_delete=models.CASCADE, related_name="task_username")
    app = models.ForeignKey(
        AndroidAppModel, on_delete=models.CASCADE, related_name="task_app")

    task_img = models.ImageField(upload_to="tasks/")

    def __str__(self):
        return str(self.user)
