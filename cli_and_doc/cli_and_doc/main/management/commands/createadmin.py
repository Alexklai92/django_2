from django.contrib.auth.management.commands.createsuperuser import Command as Createsuperuser

import getpass
import sys

from django.contrib.auth import get_user_model
from django.contrib.auth.management import get_default_username
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS
from django.utils.text import capfirst


class NotRunningInTTYException(Exception):
    pass


class Command(Createsuperuser):
    help = 'Create admin user.'

    def handle(self, *args, **options):
        username = options[self.UserModel.USERNAME_FIELD]
        database = options['database']

        password = None
        user_data = {}

        fake_user_data = {}
        verbose_field_name = self.username_field.verbose_name

        if not options['interactive']:
            try:
                if not username:
                    raise CommandError("You must use --%s with --noinput." % self.UserModel.USERNAME_FIELD)
                username = self.username_field.clean(username, None)

                for field_name in self.UserModel.REQUIRED_FIELDS:
                    if options[field_name]:
                        field = self.UserModel._meta.get_field(field_name)
                        user_data[field_name] = field.clean(options[field_name], None)
                    else:
                        raise CommandError("You must use --%s with --noinput." % field_name)
            except exceptions.ValidationError as e:
                raise CommandError('; '.join(e.messages))

        else:
            default_username = get_default_username()
            try:

                if hasattr(self.stdin, 'isatty') and not self.stdin.isatty():
                    raise NotRunningInTTYException("Not running in a TTY")

                while username is None:
                    input_msg = capfirst(verbose_field_name)
                    if default_username:
                        input_msg += " (leave blank to use '%s')" % default_username
                    username_rel = self.username_field.remote_field
                    input_msg = '%s%s: ' % (
                        input_msg,
                        ' (%s.%s)' % (
                            username_rel.model._meta.object_name,
                            username_rel.field_name
                        ) if username_rel else ''
                    )
                    username = self.get_input_data(self.username_field, input_msg, default_username)
                    if not username:
                        continue
                    if self.username_field.unique:
                        try:
                            self.UserModel._default_manager.db_manager(database).get_by_natural_key(username)
                        except self.UserModel.DoesNotExist:
                            pass
                        else:
                            self.stderr.write("Error: That %s is already taken." % verbose_field_name)
                            username = None

                if not username:
                    raise CommandError('%s cannot be blank.' % capfirst(verbose_field_name))

                for field_name in self.UserModel.REQUIRED_FIELDS:
                    field = self.UserModel._meta.get_field(field_name)
                    user_data[field_name] = options[field_name]
                    while user_data[field_name] is None:
                        message = '%s%s: ' % (
                            capfirst(field.verbose_name),
                            ' (%s.%s)' % (
                                field.remote_field.model._meta.object_name,
                                field.remote_field.field_name,
                            ) if field.remote_field else '',
                        )
                        input_value = self.get_input_data(field, message)
                        user_data[field_name] = input_value
                        fake_user_data[field_name] = input_value

                        if field.remote_field:
                            fake_user_data[field_name] = field.remote_field.model(input_value)

                while password is None:
                    password = getpass.getpass()
                    password2 = getpass.getpass('Password (again): ')
                    if password != password2:
                        self.stderr.write("Error: Your passwords didn't match.")
                        password = None
                        continue

                    if password.strip() == '':
                        self.stderr.write("Error: Blank passwords aren't allowed.")
                        password = None
                        continue

            except KeyboardInterrupt:
                self.stderr.write("\nOperation cancelled.")
                sys.exit(1)

            except NotRunningInTTYException:
                self.stdout.write(
                    "Superuser creation skipped due to not running in a TTY. "
                    "You can run `manage.py createsuperuser` in your project1 "
                    "to create one manually."
                )

        if username:
            user_data[self.UserModel.USERNAME_FIELD] = username
            user_data['password'] = password
            self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)
            if options['verbosity'] >= 1:
                self.stdout.write("Superuser created successfully.")
