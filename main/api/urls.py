from django.urls import path
from .views import *

urlpatterns = [
    path("todolist/", TodolistListAPIView.as_view()),
    path("todolist/detail/<pk>/", TodolistRetrieveAPIView.as_view()),
    path("todolist/", TodolistCreateApiView.as_view()),
    path("todolist/remove/<pk>/", TodolistDestroyAPIView.as_view()),
    path("todolist/update/<pk>/", TodolistUpdateAPIView.as_view()),
]
