import json
from django.shortcuts import render

from .models import Product 

def product_list(request):
    # context = {} 

    # with open('products/data/products.json', 'r') as file:
    #     context = json.load(file)

    # return render(request, 'products/list.html', context)

    query = Product.objects.all()

    return render(request, 'products/list.html', {'products':query})

#TODO Get only one product
def product_detail(request, pk):
    # context = {}

    # with open('products/data/products.json', 'r') as file:
    #     context = json.load(file)

    # return render(
    #     request,
    #     'products/detail.html',
    #     {
    #         'object': context['products'][idx]
    #     }
    # )

    obj = Product.objects.get(id=pk)

    return render(request, 'products/detail.html', {'object':obj})
