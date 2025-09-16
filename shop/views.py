from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.db import transaction

def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "product_list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        # increment quantity but do not exceed stock
        if item.quantity < product.stock:
            item.quantity += 1
            item.save()
    return redirect("view_cart")

@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart.html", {"cart": cart})

@login_required
def remove_from_cart(request, pk):
    # pk = CartItem id
    item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    item.delete()
    return redirect("view_cart")

@login_required
def update_cart_item(request, pk):
    # pk = CartItem id; expects POST with 'quantity'
    item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    if request.method == "POST":
        try:
            qty = int(request.POST.get("quantity", 1))
            if qty <= 0:
                item.delete()
            else:
                # enforce stock limit
                item.quantity = min(qty, item.product.stock)
                item.save()
        except ValueError:
            pass
    return redirect("view_cart")

@login_required
def checkout(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    # Placeholder: show summary and button to go to payments (Week 3)
    if request.method == "POST":
        # Normally: create Order record and redirect to payment
        return redirect("payment_placeholder")
    return render(request, "checkout.html", {"cart": cart})
