import json

import requests
import django.db
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from index.models import User

FAKE_USERS_REQUEST_URL = 'https://randomuser.me/api?results=%(requested_results)d&inc=name,email,login,registered&nat=US&noinfo'


class Command(BaseCommand):
    help = 'Generate a specified number of fake users '\
           'and save it into database.'

    def add_arguments(self, parser):
        parser.add_argument('create_fake_users', type=int, metavar='U_NUM',
                            help="A number of users to be created.")

    def _retrieve_users(self, users_number):
        url = FAKE_USERS_REQUEST_URL % {'requested_results': users_number}
        print(url)
        self.stdout.write('Requesting fake users...')
        response = requests.get(url)
        self.stdout.write('Parsing API response...')
        users = json.loads(response.text)
        return users['results']

    def handle(self, *args, **options):
        users_number = int(options['create_fake_users'])
        # TODO: implement pagination
        assert users_number <= 5000, 'API support requests for maximum 5000 results.'

        try:
            users = self._retrieve_users(users_number)
        except json.JSONDecodeError:
            raise CommandError('Failed to decode response from API.')
        except requests.ConnectionError as e:
            raise CommandError('Connection error occured.')

        for user in users:
            parsed_date = timezone.datetime.strptime(user['registered'], "%Y-%m-%d %H:%M:%S")
            date_joined = timezone.make_aware(parsed_date, timezone.get_default_timezone())

            try:
                User.objects.create(
                    username=user['login']['username'],
                    first_name=user['name']['first'].capitalize(),
                    last_name=user['name']['last'].capitalize(),
                    email=user['email'],
                    password=user['login']['password'],
                    date_joined=date_joined
                )
            except django.db.utils.IntegrityError:
                self.stdout.write(self.style.WARNING('User naming conflict, skipping this user...'))

        self.stdout.write(self.style.SUCCESS('Successfully created fake users.'))
