from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

def main(request):
    context = {
        'phone_number': '+79119697705',
        'email': 'sibles.spb@yandex.ru',
        'menu': {
            'Каталог': '/catalog',
            'Услуги': '/services',
            'О нас': '/about',
            'Контакты': '/contacts'
        }
    }
    response_string = render_to_string(
        'myshop/templates/master.html',
        context
    )
    return HttpResponse(response_string)
