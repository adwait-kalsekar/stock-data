from django.db import models

# Create your models here.

class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateTimeField(null=True, blank=True)
    open = models.CharField(max_length=100)
    high = models.CharField(max_length=100)
    low = models.CharField(max_length=100)
    close = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.symbol}+{self.date}"