from django.db import migrations, models

import apps.contacts.models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0004_contact_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="avatar",
            field=models.ImageField(
                blank=True,
                max_length=255,
                null=True,
                upload_to=apps.contacts.models.get_icon_path,
                verbose_name="Avatar",
            ),
        ),
    ]
