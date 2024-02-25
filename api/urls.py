from . import views
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"create_user", views.NewUserViewSet)
router.register(r"diets", views.DietViewSet)
router.register(r"exercises", views.ExerciseViewSet)
router.register(r"routines", views.RoutineViewSet)
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"workouts", views.WorkoutViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
