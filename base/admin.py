from django.contrib import admin
from .models import Task

# Регистрация модели в админ.панел
admin.site.register(Task)
