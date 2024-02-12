from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Category, Product
from cart.forms import CartAddProductForm


def sidebar_list(request, category_slug=None):
  categories = Category.objects.all()
  products = Product.objects.filter(is_available=True)

  if category_slug:
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)

  return render(request, 'includes/header.html', {
    'categories': categories, 
    'products': products
  })


def product_list(request, category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(is_available=True)

  if category_slug:
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)

  # Show 4 products per page
  page = request.GET.get('page', 1)
  paginator = Paginator(products, 4)
  try:
    pages = paginator.page(page)
  except PageNotAnInteger:
    pages = paginator.page(1)
  except EmptyPage:
    pages = paginator.page(paginator.num_pages)

  return render(request, 'product/product_list.html', {
    'category': category, 
    'categories': categories, 
    'products': products,
    'pages': pages,
  })


@login_required
def product_detail(request, id, slug):
  product = get_object_or_404(Product, id=id, slug=slug, is_available=True)
  cart_product_form = CartAddProductForm()

  return render(request, 'product/product_details.html', {
    'product': product,
    'cart_product_form': cart_product_form
  })
