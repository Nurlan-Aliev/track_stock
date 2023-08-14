from django.urls import path
from goods_map.goods import views


urlpatterns = [
    path('', views.GoodsList.as_view(), name='good_list'),
    path('create/', views.CreateGood.as_view(), name='create_good'),
    path('<int:pk>/update/', views.UpdateGood.as_view(), name='update_good'),
    path('<int:pk>/delete/', views.DeleteGood.as_view(), name='delete_good'),
    path('<int:pk>/', views.GoodCard.as_view(), name='good_card'),
]
