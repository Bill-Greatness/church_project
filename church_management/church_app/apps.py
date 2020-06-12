from django.apps import AppConfig


class ChurchAppConfig(AppConfig):
    name = 'church_app'

    def ready(self):
        import church_app.signals
