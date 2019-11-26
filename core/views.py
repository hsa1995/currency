from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from core.serializers import CurrencySerializer
from core.models import Currency, currency_converter


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    @action(detail=True, methods=['get'])
    def rates(self, request, *args, **kwargs):
        main_currency = self.get_object()
        target_currency_id = request.data.get('target_currency')
        target_currency = Currency.objects.filter(id=target_currency_id).first()
        data = {
            'rate': currency_converter(main_currency, target_currency)
        }
        return Response(data=data, status=status.HTTP_200_OK)
