from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):
        try:
            from django.contrib.auth import get_user_model

            User = get_user_model()

            user, created = User.objects.get_or_create(
                username="sameer",
                defaults={
                    "email": "sameer@gmail.com",
                    "is_staff": True,
                    "is_superuser": True,
                },
            )

            user.is_staff = True
            user.is_superuser = True
            user.set_password("sameerkhan@123")
            user.save()

            print("Superuser ensured.")
        except Exception as e:
            print(e)
