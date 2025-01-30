from django.urls import path
from .views import (
    product_list,
    product_detail,
    add_to_cart,
    cart_detail,
    remove_from_cart,
    clear_cart,
    contact_view,
    contact_success,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]
