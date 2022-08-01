from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.contacts.models import Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = [
        'contact_name',
        'phone_value',
        'birthday_date'
    ]
    success_url = reverse_lazy('contacts:show_all')
