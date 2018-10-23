from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import datetime

def main(request):
    # template = Template(
    #     'Hello {{ name }}!'
    # )
    # context = Context({
    #     'title': 'Лиственница с берегов Байкала в Санкт-Петербурге',
    #     'subtitle': 'Пиломатериалы из лиственницы от производителя по низкой цене'
    # })
    template = get_template('main/index.html')
    context = {
        'title': 'Лиственница с берегов Байкала в Санкт-Петербурге',
        'subtitle': 'Пиломатериалы из лиственницы от производителя по низкой цене',
        'username': 'Ann',
        'is_anon': False
    }
    response_string = template.render(context)

    return HttpResponse(response_string)
    # return render(request, 'main/index.html')


def contacts(request):
    context = {
        'contacts': [
            'Contact 1',
            'Contact 2',
            'Contact 3'
        ]
    }
    response_string = render_to_string(
        'main/contacts.html',
        context
    )
    return HttpResponse(response_string)
    # return render(request, 'main/contacts.html')    


def catalog(request):
    return render(request, 'main/catalog.html')


def services(request):
    return render(request, 'main/services.html')


def about(request):
    context = {
        # 'username': 'ann'.title(),
        # 'username': 'ann',
        # 'username': 'annannnnnnnnnnnannnnnnnnnnnn'[:3], срезы
        'username': 'annannnnnnnnnnnannnnnnnnnnnn',
        'text': '''
                Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                Eius blanditiis delectus sunt sint aut ipsam dicta, voluptas modi, 
                iusto fugiat assumenda ratione obcaecati. Corporis repudiandae cupiditate maiores ex dolore rem.
            '''
    }
    return render(request, 'main/about.html', context)
    # return render(request, 'main/about.html')
