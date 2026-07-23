from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):
        try:
            from django.contrib.auth import get_user_model

            User = get_user_model()

            if not User.objects.filter(username="sameer").exists():
                User.objects.create_superuser(
                    username="sameer",
                    email="sameer@gmail.com",
                    password="your_secure_password"
                )
        except Exception:
            pass
