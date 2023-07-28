from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from e_commerce_store.cart.models import Cart
from e_commerce_store.shop.models import Product


# Create your views here.

def cart_page(request, user_id):
    cart = Cart.objects.get(user_id=user_id)
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart.html', context)


def remove_product_from_cart(request, product_id):
    product = Product.objects.filter(pk=product_id).get()
    product.cart_id = ''
    product.save()
    return redirect('cart-page', user_id=request.user.pk)


def checkout_page(request):
    return render(request, 'cart/checkout.html')
