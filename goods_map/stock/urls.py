from django.urls import path
from goods_map.stock.views import StockView

urlpatterns = [
    path('<pk:int>/', StockView.as_view(), name='storage')
]