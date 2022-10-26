from django.contrib import admin
from .models import Task
from .models import AdvUser

admin.site.register(Task)
admin.site.register(AdvUser)