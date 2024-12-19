from django.apps import AppConfig

# Тип поля для автоматически добавляемых первичных ключей и
# Уникальное имя приложения
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
