from django.contrib import admin
from .models import Task

# Регистрация модели в административной панели Django
admin.site.register(Task)
