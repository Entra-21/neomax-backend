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
    id = serializers.IntegerField()

    class Meta:
        model = models.Exercise
        fields = ["id", "name", "gif", "muscle_group"]


class ExerciseSessionSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = models.ExerciseSession
        fields = ["id", "exercise", "reps", "sets", "weight"]

    def create(self, validated_data):
        exercise_data = validated_data.pop("exercise")
        exercise_id = exercise_data.get("id")
        print("Exercise id:", exercise_data)
        exercise = models.Exercise.objects.get(id=exercise_id)
        instance = models.ExerciseSession.objects.create(
            exercise=exercise, **validated_data
        )
        return instance


class RoutineSerializer(serializers.ModelSerializer):
    sessions = ExerciseSessionSerializer(many=True)

    class Meta:
        model = models.Routine
        fields = ["id", "title", "workout", "sessions"]

    def update(self, instance, validated_data):
        sessions_data = validated_data.pop("sessions", None)
        if sessions_data is not None:
            instance.sessions.all().delete()
            for session_data in sessions_data:
                session_serializer = ExerciseSessionSerializer(data=session_data)
                session_serializer.is_valid(raise_exception=True)
                session_serializer.save(routine=instance)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        sessions_data = validated_data.pop("sessions")
        routine = models.Routine.objects.create(**validated_data)
        for session_data in sessions_data:
            models.ExerciseSession.objects.create(routine=routine, **session_data)
        return routine


class WorkoutSerializer(serializers.ModelSerializer):
    routines = RoutineSerializer(many=True)

    class Meta:
        model = models.Workout
        fields = "__all__"

    def create(self, validated_data):
        routines_data = validated_data.pop("routines")
        workout = models.Workout.objects.create(**validated_data)
        for routine_data in routines_data:
            models.Routine.objects.create(workout=workout, **routine_data)
        return workout


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Meal
        fields = "__all__"


class DaySerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = models.Day
        fields = "__all__"

    def create(self, validated_data):
        meals_data = validated_data.pop("meals")
        day = models.Day.objects.create(**validated_data)
        for meal_data in meals_data:
            models.Meal.objects.create(day=day, **meal_data)
        return day


class DietSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True)

    class Meta:
        model = models.Diet
        fields = "__all__"

    def create(self, validated_data):
        days_data = validated_data.pop("days")
        diet = models.Diet.objects.create(**validated_data)
        for day_data in days_data:
            models.Day.objects.create(diet=diet, **day_data)
        return diet
