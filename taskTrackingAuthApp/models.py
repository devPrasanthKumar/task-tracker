from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid


# created a custom user

class User(AbstractUser):
    ''' 
    1. user_role = it means , A user can be  either admin_user or normal_user 
    it's their choice they can choose admin role or user role.

    2.  USERNAME_FIELD = 'email' : it means user can loging with their email not username

    '''
    USER_ROLE = [("Admin", "Admin"), ("NormalUser", "Normal-User")]
    email = models.EmailField(unique=True)
    user_role = models.CharField(
        choices=USER_ROLE, max_length=10, default="NormalUser")
    # implemented uuid for user for security purpose,it will be considered as pk
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
