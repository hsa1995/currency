from rest_framework.routers import DefaultRouter

from django.urls import path, include

from core.views import CurrencyViewSet


router = DefaultRouter()
router.register('currency', CurrencyViewSet, base_name='currency')

urlpatterns = [
    path('', include(router.urls))
]