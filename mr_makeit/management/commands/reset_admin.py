from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Reset the password for the admin user"

    def handle(self, *args, **kwargs):
        username = "sanda"
        new_password = "30591417"

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Password reset for {username}"))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User '{username}' does not exist"))
