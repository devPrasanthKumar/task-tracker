from django.contrib import admin


from .models import User


# customize our admin page
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "username"]
