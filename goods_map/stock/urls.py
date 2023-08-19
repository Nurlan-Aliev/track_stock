from django.urls import path
from goods_map.stock.views import CreateStock, CreateMarket, StockHome

urlpatterns = [
    path('', StockHome.as_view(), name='stock_home'),
    path('create_stock/', CreateStock.as_view(), name='create_stock'),
    path('create_market/', CreateMarket.as_view(), name='create_market')
]
