from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "contact_name",
                    models.CharField(help_text="It is name of contact", max_length=50, verbose_name="Contact name"),
                ),
                (
                    "phone_value",
                    models.PositiveBigIntegerField(
                        help_text="Phone number of contact", max_length=10, verbose_name="Phone number"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]