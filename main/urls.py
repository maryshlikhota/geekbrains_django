from django.urls import path

from main.views import (
    main, contacts, about
)

urlpatterns = [
    path('contacts/', contacts),
    path('about/', about),
    path('', main)
]
