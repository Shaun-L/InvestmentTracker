from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
  symbol = models.CharField(max_length=10)
  name = models.CharField(max_length=100)

class TheoreticalInvestment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  date_invested = models.DateField()
  
