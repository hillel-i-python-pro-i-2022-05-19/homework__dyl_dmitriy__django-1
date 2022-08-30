from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0002_contacttag_remove_contact_phone_value_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="contact_tag",
        ),
    ]
