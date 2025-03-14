from rest_framework import viewsets
from .models import (
    DjangoPlainDataModel,
    DjangoEncryptedDataModel,
    DjangoMixedDataModel,
)
from .serializers import (
    DjangoPlainDataModelSerializer,
    DjangoEncryptedDataModelSerializer,
    DjangoMixedDataModelSerializer,
)


class DjangoPlainDataModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD operations:
    - list() for GET /data/
    - create() for POST /data/
    - retrieve() for GET /data/<id>/
    - update() for PUT /data/<id>/
    - partial_update() for PATCH /data/<id>/
    - destroy() for DELETE /data/<id>/
    """

    queryset = DjangoPlainDataModel.objects.all()
    serializer_class = DjangoPlainDataModelSerializer


class DjangoEncryptedDataModelViewSet(viewsets.ModelViewSet):
    queryset = DjangoEncryptedDataModel.objects.all()
    serializer_class = DjangoEncryptedDataModelSerializer


class DjangoMixedDataModelViewSet(viewsets.ModelViewSet):
    queryset = DjangoMixedDataModel.objects.all()
    serializer_class = DjangoMixedDataModelSerializer
