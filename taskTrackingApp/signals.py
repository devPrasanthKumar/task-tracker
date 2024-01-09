from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from taskTrackingApp.models import UserProfileModel


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    '''
    it will create the profile automatically for the corresponding user when that user created an account,
    that user don't have to create a profile manually.
    '''

    if created:
        UserProfileModel.objects.create(
            user=instance, username=instance.username, user_email=instance.email)
