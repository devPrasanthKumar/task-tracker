from django.apps import AppConfig


class TasktrackingappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "taskTrackingApp"

    # added my signals here

    def ready(self):
        import taskTrackingApp.signals
