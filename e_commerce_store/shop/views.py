from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from e_commerce_store.cart.models import Cart
from e_commerce_store.shop.forms import CreateFruitForm, EditFruitForm
from e_commerce_store.shop.models import Product


# Create your views here.


def shop_page(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'shop/shop.html', context)


def single_product_page(request, pk):
    product = Product.objects.get(pk=pk)
    description = product.description
    if product.description is None:
        description = 'No information'
    context = {
        'product': product,
        'description': description,
    }
    return render(request, 'shop/single-product.html', context)


class CreateProduct(views.CreateView, LoginRequiredMixin):
    template_name = 'shop/create-product.html'
    form_class = CreateFruitForm
    success_url = reverse_lazy('shop-page')


class EditProductView(views.UpdateView, LoginRequiredMixin):
    model = Product
    template_name = 'shop/edit-product.html'
    form_class = EditFruitForm

    def get_success_url(self):
        return reverse_lazy('single-product-page', kwargs={'pk': self.object.pk})


class DeleteProductView(views.DeleteView, LoginRequiredMixin):
    template_name = 'shop/delete-product.html'
    model = Product

    def post(self, *args, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect('shop-page')


@login_required
def add_to_cart(request, product_id):
    # Get the currently logged-in user
    user = request.user

    # Get or create a cart for the user
    cart, created = Cart.objects.get_or_create(user_id=user.pk)

    # Now you can add products to this cart
    # For example, to add a fruit product to the cart:
    fruit_product = Product.objects.get(pk=product_id)
    fruit_product.cart_id = cart.pk
    fruit_product.save()

    return redirect('cart-page', user_id=user.pk)
