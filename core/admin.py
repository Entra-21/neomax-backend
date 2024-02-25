from django.contrib import admin
from .models import (
    CustomUser,
    Day,
    Diet,
    Exercise,
    ExerciseSession,
    Meal,
    Routine,
    Workout,
)


admin.site.register(
    [CustomUser, Day, Diet, Exercise, ExerciseSession, Meal, Routine, Workout]
)
