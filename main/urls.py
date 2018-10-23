from django.urls import path

from main.views import (
    main, contacts, catalog, services, about, base
)

urlpatterns = [
    path('contacts/', contacts),
    path('catalog/', catalog),
    path('services/', services),
    path('about/', about),
    path('', main)
]
