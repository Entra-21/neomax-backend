from django.contrib import admin
from core.models import Exercise, Routine, Workout, Meal, Day, Diet, CustomUser


admin.site.register([Exercise, Routine, Workout, Meal, Day, Diet, CustomUser])
