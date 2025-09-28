from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.utils import OperationalError


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        try:
            if not User.objects.filter(username="oxfordform").exists():
                User.objects.create_superuser(
                    username="oxfordform",
                    password="oxford@1",
                    email="oxfordlawfirm5@gmail.com"
                )
                print("✅ Superuser 'oxfordform' created")
        except OperationalError:
            # Happens when DB is not migrated yet
            pass
        except Exception as e:
            print("⚠️ Skipped superuser creation:", e)