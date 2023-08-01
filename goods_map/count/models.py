from django.db import models
from goods_map.goods.models import GoodsModel


class CountGoods(models.Model):
    datetime = models.DateField(auto_now=True)
    count = models.PositiveSmallIntegerField()
    good_id = models.ForeignKey(GoodsModel, on_delete=models.CASCADE)
    cost_price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.good_id
