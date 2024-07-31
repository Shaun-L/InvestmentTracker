from rest_framework import serializers
from .models import Stock, TheoreticalInvestment

class StockSerializer(serializers.ModelSerializer):
  class Meta:
    model = Stock
    fields = ['id', 'symbol', 'name']

class TheoreticalInvestmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = TheoreticalInvestment
    fields = ['id', 'stock', 'amount', 'date_invested']