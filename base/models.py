from django.db import models
from django.contrib.auth.models import User

# Структура съхранения дан. в бд
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

# Връщаме текстово представяне на задачата под формата на заглавие
    def __str__(self):
        return self.title

# Определяме клас, в който сортираме задачите по статуса на изпълнение
    class Meta:
        ordering = ['complete']

