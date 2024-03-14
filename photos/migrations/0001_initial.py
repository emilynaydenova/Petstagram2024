# Generated by Django 5.0.1 on 2024-03-06 07:57

import django.core.validators
import photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                    "photo",
                    models.ImageField(
                        upload_to="pet_photos/",
                        validators=[
                            photos.validators.ValidateFileMaxSizeInMb(max_size=5)
                        ],
                        verbose_name="Pet photo",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=300,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=30, null=True)),
                ("date_of_publication", models.DateField(auto_now=True)),
                ("tagged_pets", models.ManyToManyField(blank=True, to="pets.pet")),
            ],
        ),
    ]