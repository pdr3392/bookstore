from django.urls import path, include
from rest_framework import routes

from order import viewsets


router = routes.SimpleRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")


urlpatterns = [path("", include(router.urls))]
