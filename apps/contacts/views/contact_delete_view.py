from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.contacts.models import Contact


class ContactDeleteView(DeleteView):
    queryset = Contact.objects.all()
    success_url = reverse_lazy("contacts:show_contacts")
