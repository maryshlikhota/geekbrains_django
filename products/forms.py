from django.forms import ModelForm

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'category', 'image',
            'snippet', 'cost'
        ]
