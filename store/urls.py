from django.urls import path
from . import views
from store.views   import store, cart,checkout

urlpatterns = [
    path('',views.store, name = 'store'),
    path('cart/',views.cart, name = 'cart'),
    path('checkout/',views.checkout, name = 'checkout')
] 