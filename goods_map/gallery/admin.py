from django.contrib import admin
from .models import ImageModel


# Register your models here.
@admin.register(ImageModel)
class GoodsAdmin(admin.ModelAdmin):
    pass
