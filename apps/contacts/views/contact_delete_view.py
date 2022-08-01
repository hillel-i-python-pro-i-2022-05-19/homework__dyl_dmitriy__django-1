from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.contacts.models import Contact


class DeleteContactsView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:show_all')
