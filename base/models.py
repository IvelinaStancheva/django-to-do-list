from django.db import models
from django.contrib.auth.models import User

# Структура хранения данных в базе данных
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

# Возвращаем строковое представление задачи в виде заголовка
    def __str__(self):
        return self.title

# Определяем класс, в котором сортируем задачи по статусу выполнения
    class Meta:
        ordering = ['complete']

