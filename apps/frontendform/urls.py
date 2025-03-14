from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DjangoPlainDataModelViewSet,
    DjangoEncryptedDataModelViewSet,
    DjangoMixedDataModelViewSet,
)

# Create a router and register the viewset
router = DefaultRouter()
router.register(r"plain-data", DjangoPlainDataModelViewSet, basename="plain-datamodel")
router.register(
    r"encrypted-data", DjangoEncryptedDataModelViewSet, basename="encrypted-datamodel"
)
router.register(r"mixed-data", DjangoMixedDataModelViewSet, basename="mixed-datamodel")

urlpatterns = [
    path("", include(router.urls)),
]
