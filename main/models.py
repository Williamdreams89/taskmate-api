from django.db import models
from django.utils import timezone


# Create your models here.


class TaskmateUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)


class Todolist(models.Model):
    owner = models.ForeignKey(on_delete=models.CASCADE, to=TaskmateUser)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    starts = models.TimeField(default=timezone.now())
    ends = models.TimeField(default=timezone.now())


    def __str__(self):
        return "{} - ({})".format(self.title, self.owner)
    