import datetime

from django.db import models
from django.urls import reverse_lazy

from apps.contacts.utils import phone_regex


class TagsChoices(models.TextChoices):
    FAMILY = 'family', '#family'
    FRIENDS = 'friends', '#friends'
    TRIP = 'trip', '#trip_to_planet_c-137'


class Tags(models.Model):
    tag_name = models.CharField(
        'Tags', max_length=50, help_text="Contact's tags",
    )

    def __str__(self) -> str:
        return f"{self.tag_name}"

    __repr__ = __str__


class ContactDetailsOptions(models.Model):
    email_address = models.EmailField(
        'Email', max_length=254,
        help_text="It is the email address of the person",
        default='example@gmail.com',
        blank=True
    )
    telegram_nickname = models.CharField(
        'Telegram', max_length=100,
        help_text="Here is contact's telegram",
        blank=True
    )
    linkedin_profile = models.CharField(
        'LinkedIn', max_length=500,
        help_text="Here is the link to contact's LinkedIn profile",
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.email_address} - {self.telegram_nickname}," \
               f"- {self.linkedin_profile} "

    __repr__ = __str__


class Contact(models.Model):
    contact_name = models.CharField('Contact name', max_length=200,
                                    help_text="It is the name of the person",
                                    default='Vasya')

    tags = models.CharField(
        'Tags', max_length=50,
        help_text="Contact's personalized tags",
        choices=TagsChoices.choices,
        default=TagsChoices.TRIP,
        blank=True
    )

    tags_by_foreign_key = models.ForeignKey(
        Tags,
        related_name='contact_tags_related_by_foreign_key',
        on_delete=models.SET_NULL,
        null=True,
    )

    phone_value = models.CharField(
        'Phone number', validators=[phone_regex()], max_length=17, blank=True,
        help_text="The contact person phone number"
    )

    _time_now = datetime.datetime.now()
    birthday_date = models.DateField(
        'Date of birth',
        help_text='Please enter data in the following format %Y-%m-%d',
        default='2022-07-07',
        blank=True
    )

    contact_details_by_foreign_key = models.ForeignKey(
        ContactDetailsOptions,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy('contacts:edit', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return f"{self.contact_name} - (+{self.phone_value})"

    __repr__ = __str__
