from django.apps import AppConfig

from fruitipediaApp import fruits


class FruitsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fruitipediaApp.fruits'
