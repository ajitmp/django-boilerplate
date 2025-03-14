from django.contrib import admin
from .models import DjangoPlainDataModel, DjangoEncryptedDataModel

# Register your models here.

# admin.site.register(DjangoPlainData)


@admin.register(DjangoPlainDataModel)
class DjangoPlainDataAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "date_of_birth"]


@admin.register(DjangoEncryptedDataModel)
class DjangoEncryptedDataModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "date_of_birth"]
