from django.contrib import admin
from django.utils.html import format_html

from apps.contacts.models import Contact, Tags, ContactDetailsOptions


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'phone_value', 'tags',
                    'tags_by_foreign_key', 'birthday_date')


class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'email_address', 'telegram_nickname', 'contact_linkedin_profile'
    )

    def contact_linkedin_profile(self, obj):
        return format_html(
            f"<a href='https://www.linkedin.com/in/{obj.linkedin_profile}' "
            f"target='_blank'>"
            f"{obj.linkedin_profile}</a>"
        )


admin.site.register(Contact, ContactsAdmin)
admin.site.register(Tags)
admin.site.register(ContactDetailsOptions, ContactDetailsAdmin)
