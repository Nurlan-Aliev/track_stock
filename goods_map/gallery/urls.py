from django.urls import path
from goods_map.gallery import views


urlpatterns = [
    path('<int:pk>/add_image', views.AddImageView.as_view(), name='add_image'),
]