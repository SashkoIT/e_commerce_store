from django import forms

from e_commerce_store.common.models import Contact


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
