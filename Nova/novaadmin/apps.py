from django.apps import AppConfig

class NovaadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'novaadmin'

    def ready(self):
        from . import automation
        automation.start()
  

  