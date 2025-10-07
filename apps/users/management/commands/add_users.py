from django.core.management.base import BaseCommand
from faker import Faker

from apps.users.models import Users

fake = Faker()

class Command(BaseCommand):
    help = 'Add users to branch specializations'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of users to add (default: 10)',
        )

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for _ in range(count):
            email = fake.unique.email()
            fullname = fake.name()
            role = Users.Role.USER
            user = Users.objects.create(
                email=email,
                fullname=fullname,
                role=role
            )
            user.set_password('1234')  # Set a default password
            user.save()
            self.stdout.write(self.style.SUCCESS(f'User {email} created successfully.'))