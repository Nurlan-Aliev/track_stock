from django.contrib import admin
from .models import GoodsModel


# Register your models here.
@admin.register(GoodsModel)
class GoodsAdmin(admin.ModelAdmin):
    pass
