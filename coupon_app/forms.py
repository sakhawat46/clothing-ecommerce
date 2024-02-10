import code
from django import forms

from coupon_app.models import Coupon
from django.utils.translation import ugettext_lazy as _

class CouponCodeForm(forms.Form):
    code = forms.CharField(label="Enter Coupon Code" )