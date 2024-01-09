from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from taskTrackingApp.models import UserProfileModel

# create a serializer for serializing user's email and password


class UserAccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "password", "username", "user_role"]

    '''
    override the create method for hasing user's password 
    converts raw passwords to encoded format
    '''

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data["password"])
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    user_role = UserAccountCreateSerializer(read_only=True)

    class Meta:
        model = UserProfileModel
        fields = ["username", "user_email", "user_role"]
