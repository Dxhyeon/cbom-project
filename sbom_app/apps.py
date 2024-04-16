from django.apps import AppConfig


class SbomAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sbom_app'
    
    def ready(self):
        from . import tasks 
        tasks.start()
