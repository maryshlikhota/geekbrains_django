from django.urls import path

from main.views import (
    main, contacts, catalog, services, about
)

app_name = 'main'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog, name='catalog'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('', main, name='index')
]
