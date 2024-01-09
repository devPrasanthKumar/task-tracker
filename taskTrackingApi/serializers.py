from rest_framework import serializers
from rest_framework.validators import ValidationError
from taskTrackingApp.models import AndroidAppModel,  TaskModel


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskModel
        fields = ["task_img"]


class AndroidAppSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    tasks = TaskSerializer(many=True, read_only=True, source='task_app')

    class Meta:
        model = AndroidAppModel
        fields = "__all__"

    def validate(self, validated_data):
        points_length = validated_data["points"]
        if int(points_length) > 1000:
            raise ValidationError(
                {"Message": "Points Should be below 1000"})
        return super().validate(validated_data)


class UserPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidAppModel
        fields = ["points"]
