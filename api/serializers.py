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


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = "__all__"


class ExerciseSessionSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    class Meta:
        model = models.ExerciseSession
        fields = "__all__"


class RoutineSerializer(serializers.ModelSerializer):
    sessions = ExerciseSessionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Routine
        fields = "__all__"


class WorkoutSerializer(serializers.ModelSerializer):
    routines = RoutineSerializer(many=True, read_only=True)

    class Meta:
        model = models.Workout
        fields = "__all__"


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Diet
        fields = "__all__"
