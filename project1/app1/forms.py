from django import forms
from .models import Category,Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','image','number']


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name','description','price','image'] #adjust field as per your product model


