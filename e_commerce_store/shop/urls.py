from django.urls import path
from e_commerce_store.shop.views import *

urlpatterns = [
    path('', shop_page, name='shop-page'),
    path('<int:pk>', single_product_page, name='single-product-page'),
    path('create-product/', CreateProduct.as_view(), name='create-product-page'),
    path('edit-product/<int:pk>/', EditProductView.as_view(), name='edit-product-page'),
    path('delete-product/<int:pk>/', DeleteProductView.as_view(), name='delete-product-page'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart-page'),
]
