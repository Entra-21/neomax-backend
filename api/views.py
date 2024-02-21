from rest_framework import viewsets, mixins
from rest_framework.response import Response
from api import serializers
from core import models


class NewUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.NewUserSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)