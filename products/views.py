import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import Http404

from .forms import ProductForm
from .models import Product


def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    success_url = reverse_lazy('main:index')

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, 'products/delete.html', {'obj': obj})


def product_update(request, pk):
    # try:
    #     obj = Product.objects.get(pk=pk)
    # except Exception as err:
    #     raise Http404
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=obj)
    success_url = reverse_lazy('main:index')

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/update.html',
        {
            'form': form,
            'obj': obj
        }
    )


def product_create(request):
    form = ProductForm()
    success_url = reverse_lazy('main:index')

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def product_list(request):
    # context = {}

    # with open('products/data/products.json', 'r') as file:
    #     context = json.load(file)

    # return render(request, 'products/list.html', context)

    # query = Product.objects.all()

    query = get_list_or_404(Product)
    page = request.GET.get('page')
    paginator = Paginator(query, 12)

    products = paginator.get_page(page)

    return render(request, 'products/list.html', {'products': products})


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

    # obj = Product.objects.get(id=pk)

    obj = get_object_or_404(Product, pk=pk)

    return render(request, 'products/detail.html', {'object': obj})
