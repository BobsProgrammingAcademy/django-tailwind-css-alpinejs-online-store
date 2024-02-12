from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  postal_code = models.CharField(max_length=50)
  country = models.CharField(max_length=200)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  is_paid = models.BooleanField(default=True)

  def __str__(self):
    return f'Order {self.id}'
  

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.PositiveIntegerField(default=1)

  def __str__(self):
    return str(self.id)
  
  def get_cost(self):
    return self.price * self.quantity
