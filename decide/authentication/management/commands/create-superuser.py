"""

create-superuser.py is copied from:
https://gist.github.com/c00kiemon5ter/7806c1eac8c6a3e82f061ec32a55c702
with a little change becouse our user has been overwriten

****************************************
Extend createsuperuser command to allow non-interactive creation of a
superuser with a password.

Example usage:
  manage.py create-superuser \
          --password foo     \
          --email foo@foo.foo
"""
from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = 'Create a superuser with a password non-interactively'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--password', dest='password', default=None,
            help='Specifies the password for the superuser.',
        )

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        database = options.get('database')
        password = options.get('password')
        email = options.get('email')

        if not password or not email:
            raise CommandError(
                    "--email and --password are required options")

        user_data = {
           
            'password': password,
            'email': email,
        }

        self.UserModel._default_manager.db_manager(
                database).create_superuser(**user_data)

        if options.get('verbosity', 0) >= 1:
            self.stdout.write("Superuser created successfully.")