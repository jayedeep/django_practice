from django.apps import AppConfig


class CustomauthenticateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customauthenticate'

    def ready(self):
        import customauthenticate.signals