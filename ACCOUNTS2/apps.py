from django.apps import AppConfig


class Accounts2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ACCOUNTS2'

    def ready(self):
        import ACCOUNTS2.signals
