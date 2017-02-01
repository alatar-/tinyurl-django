from django.core.management.base import BaseCommand, CommandError
from users.models import User


class Command(BaseCommand):
    help = 'Generate a specified number of fake users '\
           'and save it into database.'

    def add_arguments(self, parser):
        parser.add_argument('create_fake_users', type=int, metavar='U_NUM',
                            help="A number of users to be created.")

    def handle(self, *args, **options):
        pass
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))
