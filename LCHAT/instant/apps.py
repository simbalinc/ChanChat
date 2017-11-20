from django.apps import AppConfig


class InstantConfig(AppConfig):
    name = 'instant'

    def ready(self):
        import instant.signals
