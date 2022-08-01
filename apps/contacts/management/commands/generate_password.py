import random
import string
from typing import ClassVar, Final

from django.core.management.base import BaseCommand, CommandParser
from faker import Faker

fake = Faker()

PASSWORD_CHARACTERS: Final[str] = "".join(
    [
        string.ascii_letters,
        string.digits,
    ]
)


def generate_password(password_length: int = 64) -> str:
    password_as_list = [
        random.choice(PASSWORD_CHARACTERS) for _ in range(password_length)
    ]
    random.shuffle(password_as_list)
    return "".join(password_as_list)


class Command(BaseCommand):
    HELP_TEXT: ClassVar[str] = 'Generates random 64 length string'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('length', type=int)

    def handle(self, *args, **options):
        password_length: int = options['length']
        print(generate_password(password_length=password_length))
