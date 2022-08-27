import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactTag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tag", models.CharField(help_text="Name of contact tag", max_length=50, verbose_name="Tag")),
            ],
        ),
        migrations.RemoveField(
            model_name="contact",
            name="phone_value",
        ),
        migrations.AddField(
            model_name="contact",
            name="birthday",
            field=models.DateField(blank=True, help_text="Date of birth", null=True, verbose_name="Birthday"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="contact_name",
            field=models.CharField(help_text="Name of contact", max_length=50, verbose_name="Contact name"),
        ),
        migrations.CreateModel(
            name="ContactData",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "contact_type",
                    models.CharField(
                        choices=[
                            ("PHONE_NUMBER", "Phone Number"),
                            ("EMAIL_ADDRESS", "Email Address"),
                            ("TELEGRAM_NICKNAME", "Telegram Nickname"),
                            ("LINKEDIN_ID", "LinkedIn ID"),
                        ],
                        default="PHONE_NUMBER",
                        max_length=30,
                        verbose_name="Contact type",
                    ),
                ),
                ("value", models.CharField(default="", max_length=100, verbose_name="Value")),
                (
                    "contact",
                    models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to="contacts.contact"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contact",
            name="contact_tag",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="contacts.contacttag"
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="contact_tags",
            field=models.ManyToManyField(blank=True, related_name="contact_tags", to="contacts.contacttag"),
        ),
    ]
