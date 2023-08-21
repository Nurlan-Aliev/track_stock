from django.contrib import admin
from .models import StockModel, StoreHall, StoreBack, StoreUp


# Register your models here.
@admin.register(StockModel, StoreHall, StoreBack, StoreUp)
class GoodsAdmin(admin.ModelAdmin):
    pass
