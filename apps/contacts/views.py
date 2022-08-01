from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


def show_all_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    return render(
        request, 'contacts/show_all.html',
        {"contacts": contacts}
    )


def create_contacts(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Contact created')
            return redirect('contacts:show_all')

    else:
        form = ContactForm()

    return render(
        request,
        'contacts/edit.html',
        {"form": form}
    )


def edit_contacts(request: HttpRequest, pk: int) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)
    if request.POST:
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            messages.info(request, 'Contact edited')
            return redirect('contacts:show_all')

    else:
        form = ContactForm(instance=contact)

    return render(
        request,
        'contacts/edit.html',
        {"form": form}
    )


def delete_contacts(request: HttpRequest, pk: int) -> HttpResponse:
    total_deleted_contacts, _ = Contact.objects.filter(pk=pk).delete()

    if total_deleted_contacts:
        messages.warning(request, f'Contact deleted: {total_deleted_contacts}')
    else:
        messages.info(request, 'Nothing deleted')

    return redirect('contacts:show_all')
