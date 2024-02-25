from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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
    
    
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = models.Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer    
    
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = models.Workout.objects.all()
    serializer_class = serializers.WorkoutSerializer
    
    
class DietViewSet(viewsets.ModelViewSet):
    queryset = models.Diet.objects.all()
    serializer_class = serializers.DietSerializer
    
    
class RoutineViewSet(viewsets.ModelViewSet):
    queryset = models.Routine.objects.all()
    serializer_class = serializers.RoutineSerializer
    
    # def perform_create(self, serializer):
    #     workout_id = self.request.data.get('workout_id')
    #     workout = get_object_or_404(models.Workout, id=workout_id)
    #     serializer.save(workout=workout)