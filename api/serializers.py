from rest_framework import serializers
from core import models


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "profile_picture",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "date_of_birth",
            "diets",
            "workouts",
        ]
