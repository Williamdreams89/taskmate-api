from django.contrib import admin

from .models import TaskmateUser, Todolist


# Register your models here.

admin.site.register(TaskmateUser)
admin.site.register(Todolist)
