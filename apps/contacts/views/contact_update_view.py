from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.contacts.models import Contact


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['contact_name', 'phone_value']
    success_url = reverse_lazy('contacts:show_all')
