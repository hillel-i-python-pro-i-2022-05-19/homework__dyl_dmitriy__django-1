from django.core.validators import RegexValidator
from django.db import models


class Contact(models.Model):
    contact_name = models.CharField('Name', max_length=200,
                                    help_text="It is the name of the person")
    _phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. "
                "Up to 15 digits allowed."
    )
    phone_value = models.CharField(
        'Phone number', validators=[_phone_regex], max_length=17, blank=True,
        help_text="The contact person phone number"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
