# Generated by Django 5.0.7 on 2025-03-14 05:08

import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("frontendform", "0003_djangoencrypteddatamodel_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DjangoMixedDataModel",
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
                ("name", models.CharField(max_length=200)),
                ("email", encrypted_model_fields.fields.EncryptedEmailField()),
                ("date_of_birth", encrypted_model_fields.fields.EncryptedDateField()),
                ("country", models.CharField(max_length=50)),
            ],
        ),
    ]
