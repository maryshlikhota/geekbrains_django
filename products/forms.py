from django.forms import ModelForm

from .models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'category', 'cost', 
            'image', 'snippet'
        ]
        

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'snippet']
