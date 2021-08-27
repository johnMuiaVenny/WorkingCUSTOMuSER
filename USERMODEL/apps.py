from django.apps import AppConfig


class UsermodelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'USERMODEL'

    def ready(self):
        import USERMODEL.signals
