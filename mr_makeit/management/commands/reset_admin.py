from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import django

class Command(BaseCommand):
    help = "Reset the password for the admin user or create it if it doesn’t exist"

    def handle(self, *args, **kwargs):
        # Ensure Django is fully initialized
        django.setup()

        User = get_user_model()  # Ensures it works with custom User models

        username = "sanda"
        new_password = "snave1234"
        email = "snaveford@gmail.com"

        try:
            user, created = User.objects.get_or_create(username=username, defaults={"email": email})
            user.set_password(new_password)
            user.is_superuser = True  # Ensure admin privileges
            user.is_staff = True
            user.save()

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created superuser {username}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Password reset for {username}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {str(e)}"))
