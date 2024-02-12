from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from store.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@login_required
@require_POST
def cart_add(request, product_id):
  cart = Cart(request)
  product = get_object_or_404(Product, id=product_id)
  form = CartAddProductForm(request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
  return redirect('cart:cart_detail')


@login_required
@require_POST
def cart_remove(request, product_id):
  cart = Cart(request)
  product = get_object_or_404(Product, id=product_id)
  cart.remove(product)
  return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
  cart = Cart(request)
  for item in cart:
    item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
  return render(request, 'cart/cart_details.html', {'cart': cart})