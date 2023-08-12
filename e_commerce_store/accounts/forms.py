from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from e_commerce_store.accounts.models import FruitStoreUser


class FruitStoreUserUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = FruitStoreUser
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}), )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'}),
    )
    error_messages = {
        'invalid_login': "Please enter a correct username and password."
    }


class FruitStoreUserEditForm(forms.ModelForm):
    class Meta:
        model = FruitStoreUser
        fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'profile_picture', 'phone_number',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'gender': 'Gender',
            'phone_number': 'Phone Number',
        }
        widgets = {
            'phone_number': forms.TextInput()
        }
