from django.db import models

from encrypted_model_fields.fields import (
    EncryptedCharField,
    EncryptedEmailField,
    EncryptedDateField,
)


# Create your models here.


class DjangoPlainDataModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class DjangoEncryptedDataModel(models.Model):
    name = EncryptedCharField(max_length=200)
    email = EncryptedEmailField()
    date_of_birth = EncryptedDateField()

    def __str__(self):
        return self.name


class DjangoMixedDataModel(models.Model):
    name = models.CharField(max_length=200)
    email = EncryptedEmailField()
    date_of_birth = EncryptedDateField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name
