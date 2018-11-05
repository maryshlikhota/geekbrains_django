from django.urls import path

from products.views import (
    ProductCreate, ProductUpdate, ProductDelete,
    ProductList, ProductDetail,
    product_create, product_update, product_delete,
    product_list, product_detail
)


app_name = 'products'

urlpatterns = [
    path('<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='update'),
    path('create/', ProductCreate.as_view(), name='create'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='index'),
]
