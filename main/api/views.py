from rest_framework.generics import (CreateAPIView,ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView)

from ..models import TaskmateUser, Todolist
from .serializers import TodolistSerializer, TaskmateUserSerializer


class TodolistListAPIView(ListAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()

class TodolistCreateApiView(CreateAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()

    
class TodolistListAPIView(ListAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()

    
class TodolistRetrieveAPIView(RetrieveAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()


class TodolistUpdateAPIView(UpdateAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()


class TodolistDestroyAPIView(DestroyAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()


class TaskmateUserCreateApiView(CreateAPIView):
    serializer_class = TaskmateUserSerializer
    queryset = TaskmateUser.objects.all()

    
class TaskmateUserRetrieveAPIView(RetrieveAPIView):
    serializer_class = TaskmateUserSerializer
    queryset = TaskmateUser.objects.all()


class TaskmateUserUpdateAPIView(UpdateAPIView):
    serializer_class = TaskmateUserSerializer
    queryset = TaskmateUser.objects.all()


class TaskmateUserDestroyAPIView(DestroyAPIView):
    serializer_class = TaskmateUserSerializer
    queryset = TaskmateUser.objects.all()