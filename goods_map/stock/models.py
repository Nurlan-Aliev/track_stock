from django.db import models


class StockModel(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class MarketModel(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
