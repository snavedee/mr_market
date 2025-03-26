from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Reset the password for the admin user or create it if it doesn’t exist"

    def handle(self, *args, **kwargs):
        username = "sanda"
        new_password = "30591417"
        email = "snaveford@gmail.com"

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Password reset for {username}"))
        except User.DoesNotExist:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=new_password
            )
            self.stdout.write(self.style.SUCCESS(f"Created superuser {username}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))