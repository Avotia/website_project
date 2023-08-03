from django.apps import AppConfig

VERBOSE_APP_NAME = 'Объявления'

class AppAdvertisementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_advertisements'
    verbose_name = VERBOSE_APP_NAME
