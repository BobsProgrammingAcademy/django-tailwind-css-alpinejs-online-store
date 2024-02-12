from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


@login_required
def order_create(request):
  cart = Cart(request)
  if request.method == 'POST':
    form = OrderCreateForm(request.POST, user=request.user)
    if form.is_valid():
      order = form.save()
      for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'],quantity=item['quantity'])
      # clear the cart
      cart.clear()
      return render(request, 'order/order_created.html', {'order': order})
  else:
    form = OrderCreateForm(user=request.user)
  return render(request, 'order/create_order.html', {'cart': cart, 'form': form})
