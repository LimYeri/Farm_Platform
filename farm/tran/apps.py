from django.apps import AppConfig


class TranConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tran"

    def ready(self):
        import tran.templatetags.custom
