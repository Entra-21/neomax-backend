from django.contrib import admin
from .models import Exercise, Routine, Workout, Meal, Day, Diet, CustomUser


admin.site.register([Exercise, Routine, Workout, Meal, Day, Diet, CustomUser])
