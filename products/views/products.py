import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    ListView, DetailView
)
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import Http404

from products.forms import ProductForm
from products.models import Product


class ProductCreate(CreateView):
    model = Product
    fields = [
        'title', 'category', 'cost',
        'image', 'snippet'
    ]
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:index')


class ProductUpdate(UpdateView):
    model = Product
    fields = [
        'title', 'category', 'cost',
        'image', 'snippet'
    ]
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:index')
    

class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:index')


class ProductList(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 12


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'


def product_create(request):
    form = ProductForm()
    success_url = reverse_lazy('products:index')

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def product_update(request, pk):
    # try:
    #     obj = Product.objects.get(pk=pk)
    # except Exception as err:
    #     raise Http404
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=obj)
    success_url = reverse_lazy('products:index')

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


def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    success_url = reverse_lazy('products:index')

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, 'products/delete.html', {'obj': obj})


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

    # context = {
    #     'subtitle': 'Сибирская (ангарская) лиственница — хороший выбор для создания дома вашей мечты',
    #     'text': [
    #         '''
    #                 Из имеющихся у нас различных пиломатериалов Вы можете сделать как стены (внутренняя и внешняя обшивка), так и потолок и пол.
    #                 Отлично подойдет для дома, бани, террасы или беседки. Доска лиственницы очень прочная, Вы всегда будете
    #                 уверенны, что ни перепад температур, ни влажность, ни годы ей не страшны. А приятный рисунок и многообразие
    #                 оттенков этой породы достоины того, чтобы не прятать его за краской, а гордо показать, например, под
    #                 лаком, расположив панели в любом направлении по Вашему желанию.
    #             ''',
    #         '''
    #                 Лиственница — это всегда экологично, всегда безопасно, всегда красиво.
    #             '''
    #     ],
    #     'products': products
    # }

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
