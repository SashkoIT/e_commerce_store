from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from e_commerce_store.cart.forms import OrderForm, QuantityForm
from e_commerce_store.cart.models import Cart, Order
from e_commerce_store.shop.models import Product

# Create your views here.

user_input = 0


def cart_page(request, user_id):
    cart = Cart.objects.get(user_id=user_id)
    context = {
        'cart': cart,
        'user_id': user_id,
    }
    return render(request, 'cart/cart.html', context)


def remove_product_from_cart(request, product_id):
    product = Product.objects.filter(pk=product_id).get()
    product.cart_id = ''
    product.save()
    return redirect('cart-page', user_id=request.user.pk)


# def checkout_page(request):
#     cart = Cart.objects.get(user_id=request.user.pk)
#     all_products = cart.product_set.all()
#     context = {
#         'all_products': all_products,
#     }
#     return render(request, 'cart/checkout.html', context)


class Checkout(views.CreateView):
    template_name = 'cart/checkout.html'
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('finished-order-page')
    print(user_input)

    def form_valid(self, form):
        result = super().form_valid(form)
        self.object.user_id = self.request.user.pk
        self.object.save()
        return result


def finished_order(request):
    # clear cart after successful order
    cart = Cart.objects.get(user_id=request.user.pk)
    products = Product.objects.filter(cart_id=cart.pk)
    for product in products:
        product.cart_id = ''
        product.save()

    return render(request, 'cart/successful-order.html')


def history(request):
    orders = Order.objects.filter(user_id=request.user.pk)
    context = {
        'orders': orders,
    }
    return render(request, 'cart/history.html', context)
