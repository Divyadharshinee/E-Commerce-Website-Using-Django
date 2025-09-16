from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="shop_home"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("add-to-cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/remove/<int:pk>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/update/<int:pk>/", views.update_cart_item, name="update_cart_item"),
    path("checkout/", views.checkout, name="checkout"),
    # placeholder for payment
    path("payment-placeholder/", views.product_list, name="payment_placeholder"),
]
