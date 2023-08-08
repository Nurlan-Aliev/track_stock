from django.contrib import admin
from .models import StockModel


# Register your models here.
@admin.register(StockModel)
class GoodsAdmin(admin.ModelAdmin):
    pass
