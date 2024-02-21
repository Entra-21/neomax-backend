from . import views
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"create_user", views.NewUserViewSet)
router.register(r"users", views.UserViewSet, basename="user")
# router.register(r"", views.)
# router.register(r"", views.)

urlpatterns = [
    path("api/", include(router.urls)),
]
