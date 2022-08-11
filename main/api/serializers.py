from rest_framework import serializers
from main.models import TaskmateUser, Todolist


class TaskmateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskmateUser
        fields = "__all__"

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = "__all__"