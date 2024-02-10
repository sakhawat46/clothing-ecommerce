from dataclasses import fields
from pyexpat import model
from django import forms
from payment_app.models import BillingAddress
from order_app.models import Order

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        # fields = ['first_name', 'last_name', 'country', 'address1', 'address2', 'city', 'zipcode', 'phone_number']
        fields = ('__all__')
        exclude = ('user',)


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method',]