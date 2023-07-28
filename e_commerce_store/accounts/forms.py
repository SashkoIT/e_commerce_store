from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from e_commerce_store.accounts.models import FruitStoreUser


class FruitStoreUserUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = FruitStoreUser
        fields = ('username', 'email')
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Username2'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}),
        # }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}), )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'}),
    )


class FruitStoreUserEditForm(forms.ModelForm):
    class Meta:
        model = FruitStoreUser
        fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'profile_picture',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'gender': 'Gender',
        }
