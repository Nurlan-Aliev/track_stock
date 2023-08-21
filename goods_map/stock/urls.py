from django.urls import path
from goods_map.stock.views import StockHome

urlpatterns = [
    path('', StockHome.as_view(), name='stock_home'),
]
