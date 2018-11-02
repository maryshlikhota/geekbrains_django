from django.urls import path

from .views import (
    product_list, product_detail, product_create,
    product_update, product_delete
)


app_name = 'products'

urlpatterns = [
    path('<int:pk>/delete/', product_delete, name='delete'),
    path('<int:pk>/update/', product_update, name='update'),
    path('create/', product_create, name='create'),
    path('<int:pk>/', product_detail, name='detail'),
    path('', product_list, name='index'),
]
