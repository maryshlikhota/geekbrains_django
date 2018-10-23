import json
from django.shortcuts import render


def product_list(request):
    context = {}

    with open('products/data/products.json', 'r') as file:
        context = json.load(file)

    return render(request, 'products/list.html', context)


#TODO Get only one product
def product_detail(request):
    context = {}

    with open('products/data/products.json', 'r') as file:
        context = json.load(file)

    return render(request, 'products/list.html', context)
