from django.urls import path


from products.views import (
    product_list, product_detail
)

urlpatterns = [
    path('detail/', product_detail),
    path('', product_list)
]
