# Generated by Django 4.2.5 on 2023-09-25 14:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ticket", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("headline", models.CharField(max_length=128)),
                ("body", models.TextField(blank=True, max_length=8192)),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("time_created", models.DateTimeField(auto_now_add=True)),
                (
                    "id_ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ticket.ticket"
                    ),
                ),
                (
                    "id_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
