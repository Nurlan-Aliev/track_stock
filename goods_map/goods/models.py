from django.db import modelsclass GoodsModel(models.Model):    name = models.CharField(max_length=50)    cost_price = models.PositiveSmallIntegerField()    wholesale_price = models.PositiveSmallIntegerField(null=True)    retail_price = models.PositiveSmallIntegerField(null=True)    weight = models.FloatField(null=True)    def __str__(self):        return self.name