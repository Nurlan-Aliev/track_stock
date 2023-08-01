from django.urls import path
from goods_map.stock.views import CreateStock

urlpatterns = [
    path('create/', CreateStock.as_view(), name='create_stock')
]