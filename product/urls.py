from django.urls import path, include
from rest_framework import routes

from product import viewsets


router = routes.SimpleRouter()
router.register(r"product", viewsets.ProductViewSet, basename="product")


urlpatterns = [path("", include(router.urls))]
