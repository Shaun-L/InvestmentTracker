from rest_framework import viewsets
from .models import Stock, TheoreticalInvestment
from .serializers import StockSerializer, TheoreticalInvestmentSerializer

class StockViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer

class TheoreticalInvestmentViewSet(viewsets.ModelViewSet):
  serializer_class = TheoreticalInvestmentSerializer

  def get_queryset(self):
    return TheoreticalInvestment.objects.filter(user=self.request.user)
