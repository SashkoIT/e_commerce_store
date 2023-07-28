from django.urls import path
from e_commerce_store.cart.views import *

urlpatterns = [
    path('<int:user_id>/', cart_page, name='cart-page'),
    path('remove-product/<int:product_id>/', remove_product_from_cart, name='remove-product-page'),
    path('checkout/', checkout_page, name='checkout-page'),
]
