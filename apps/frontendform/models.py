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


class DjangoEncryptedDataModel(models.Model):
    name = EncryptedCharField(max_length=200)
    email = EncryptedEmailField()
    date_of_birth = EncryptedDateField()
