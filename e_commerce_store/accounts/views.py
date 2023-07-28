from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic as views
from django.contrib.auth import views as auth_views

from e_commerce_store.accounts.forms import FruitStoreUserUserCreateForm, LoginForm, FruitStoreUserEditForm
from e_commerce_store.cart.models import Cart

# Create your views here.

UserModel = get_user_model()


class RegisterUser(views.CreateView):
    form_class = FruitStoreUserUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('landing-page')

    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        Cart.objects.create(user_id=self.object.pk)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        # return self.request.POST.get('next', self.success_url)
        return self.success_url


class LoginUser(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    # success_url = reverse_lazy('home-page')


class LogoutUser(auth_views.LogoutView, LoginRequiredMixin):
    pass


class DetailsProfile(views.DetailView, LoginRequiredMixin):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        profile_image = 'static/images/person.png'

        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)

        context['profile_image'] = profile_image
        return context


class EditUser(views.UpdateView, LoginRequiredMixin):
    model = UserModel
    form_class = FruitStoreUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class DeleteUser(views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'

    def post(self, *args, pk):
        self.request.user.delete()
        return redirect('landing-page')
