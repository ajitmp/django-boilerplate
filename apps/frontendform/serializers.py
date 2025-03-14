from rest_framework import serializers
from .models import DjangoPlainDataModel, DjangoEncryptedDataModel, DjangoMixedDataModel


class DjangoPlainDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoPlainDataModel
        fields = ["id", "name", "email", "date_of_birth"]


class DjangoEncryptedDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoEncryptedDataModel
        fields = ["id", "name", "email", "date_of_birth"]


class DjangoMixedDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMixedDataModel
        fields = ["id", "name", "email", "date_of_birth", "country"]
