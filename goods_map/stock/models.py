from django.db import models


class StockModel(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class StoreHall(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class StoreBack(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class StoreUp(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
