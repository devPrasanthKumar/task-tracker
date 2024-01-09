# Register your models here.
from django.contrib import admin

# Register your models here.
from taskTrackingApp.models import AndroidAppModel,   TaskModel, UserProfileModel


@admin.register(AndroidAppModel)
class AndroidAppAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "app_name", "points"]


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "app", "task_img"]


@admin.register(UserProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user",  "username", ]
