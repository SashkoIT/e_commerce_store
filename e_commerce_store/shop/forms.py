from django import forms

from e_commerce_store.shop.models import Product


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'picture', 'quantity', 'price', 'description', ]


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'picture', 'quantity', 'price', 'description', ]


class DeleteFruitForm(forms.ModelForm):
    pass
