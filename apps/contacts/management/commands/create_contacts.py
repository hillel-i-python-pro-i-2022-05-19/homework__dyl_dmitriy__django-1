import random
from typing import ClassVar

from django.core.management.base import BaseCommand, CommandParser
from faker import Faker

from apps.contacts.models import Contact

fake = Faker()


class Command(BaseCommand):
    HELP_TEXT: ClassVar[str] = 'Closes the specified poll for voting'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        amount_of_contacts: int = options['amount']

        for _ in range(amount_of_contacts):
            contact = Contact(
                contact_name=f'{fake.first_name()}',
                phone_value=f'{random.randint(10000000000, 999999999999)}',
            )
            contact.save()
