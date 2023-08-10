from django.db import modelsfrom goods_map.stock.models import StockModelclass GoodsModel(models.Model):    name = models.CharField(max_length=50)    images = models.ImageField(upload_to='images', null=True, blank=True)    cost_price = models.PositiveSmallIntegerField(null=True)    wholesale_price = models.PositiveSmallIntegerField(null=True)    retail_price = models.PositiveSmallIntegerField(null=True)    weight = models.FloatField(null=True)    stock = models.ManyToManyField(StockModel)    def __str__(self):        return self.name