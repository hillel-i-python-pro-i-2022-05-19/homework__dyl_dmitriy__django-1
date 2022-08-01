from django.views.generic import ListView

from apps.contacts.models import Contact


class ShowAllContactsView(ListView):
    model = Contact
    template_name = 'contacts/show_all.html'
    context_object_name = 'contacts'
