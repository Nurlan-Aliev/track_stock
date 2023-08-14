from django.db import models
from goods_map.goods.models import GoodsModel


class ImageModel(models.Model):
    product_id = models.ForeignKey(GoodsModel, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.images
