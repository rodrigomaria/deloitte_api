# Generated by Django 3.2.11 on 2022-01-24 02:25

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=100)),
                (
                    "description",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
            },
        ),
    ]