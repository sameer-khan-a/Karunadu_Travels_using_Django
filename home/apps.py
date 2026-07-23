from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):
        try:
            from django.contrib.auth import get_user_model

            User = get_user_model()

            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="sameer",
                    email="sameer@gmail.com",
                    password="sameerkhan@123"
                )
                print("✓ Admin created.")
        except Exception:
            pass
