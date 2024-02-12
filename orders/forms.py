from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ['address', 'city', 'postal_code', 'country']

  def __init__(self, *args, **kwargs):
    self._user = kwargs.pop('user')
    super(OrderCreateForm, self).__init__(*args, **kwargs)

  def save(self, commit=True):
    inst = super(OrderCreateForm, self).save(commit=False)
    inst.user = self._user
    if commit:
      inst.save()
      self.save_m2m()
    return inst
