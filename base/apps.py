from django.apps import AppConfig

# Тип на полето за автоматично добавяните първични ключове и
# Уник.име на пр.
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
