from taskTrackingApp.models import *
from django import forms


# form for creating a new app by admin
class CreateAppForm(forms.ModelForm):
    class Meta:
        model = AndroidAppModel
        fields = "__all__"
        exclude = ["user"]


class UpdateUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfileModel
        fields = ["username", "user_email"]
