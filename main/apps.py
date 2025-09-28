from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import User

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Connect the function to run after migrations
        post_migrate.connect(create_admin_user, sender=self)

def create_admin_user(sender, **kwargs):
    try:
        if not User.objects.filter(username="oxfordform").exists():
            User.objects.create_superuser(
                username="oxfordform",
                password="oxford@1",
                email="oxfordlawfirm5@gmail.com"
            )
            print("✅ Superuser 'oxfordform' created")
    except Exception as e:
        print("⚠️ Superuser creation skipped:", e)