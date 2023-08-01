from django.urls import path
from goods_map.count import views


urlpatterns = [
    path('<int:pk>/create/', views.AddGoodsView.as_view(), name='add_goods'),
    path('<int:pk>/update/', views.UpdateCount.as_view(), name='update_count'),
]
