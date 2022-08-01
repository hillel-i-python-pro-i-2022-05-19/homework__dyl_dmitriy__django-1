from typing import NamedTuple

from faker import Faker

fake = Faker()


class User(NamedTuple):
    name: str
    unique_email_address: str


def generate_users() -> User:
    return User(fake.name(), fake.unique.ascii_email())
