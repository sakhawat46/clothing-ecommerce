# from audioop import reverse
from django.urls import reverse
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

#models
from payment_app.models import BillingAddress
from payment_app.forms import BillingAddressForm, PaymentMethodForm
from order_app.models import Cart, Order


from django.conf import settings
import json

#messages
from django.contrib import messages

#view
from django.views.generic import TemplateView



from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages


# Create your views here.

class CheckoutTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user = request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)
        payment_method = PaymentMethodForm()
        order_qs = Order.objects.filter(user=request.user, ordered = False)
        if order_qs.exists():
            order_item = order_qs[0].orderitems.all()
            order_total = order_qs[0].get_totals()

            context = {
                'billing_address': form,
                'order_item': order_item,
                'order_total': order_total,
                'payment_method': payment_method
            } 
            return render(request, 'store_app/checkout.html', context)

        return redirect('order_app:cart')

    def post(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user = request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)
        payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
        payment_form = PaymentMethodForm(instance=payment_obj)
        if request.method == 'post' or request.method == 'POST':
            form = BillingAddressForm(request.POST, instance=saved_address)
            pay_form = PaymentMethodForm(request.POST, instance=payment_obj)
            if form.is_valid() and pay_form.is_valid():
                form.save()
                pay_method = pay_form.save()
                
                if not saved_address.is_fully_filled():
                    messages.warning(request, "Please Give Billing Address")
                    return redirect('checkout')

                #Cash on delivary payment process
                if pay_method.payment_method == 'Cash On Delivery':
                    order_qs = Order.objects.filter(user=request.user, ordered=False)
                    order = order_qs[0]
                    order.ordered = True
                    order.orderId = order.id
                    order.paymentId = pay_method.payment_method
                    order.save()
                    messages.success(request, "Order Successfully Completed")
                    cart_items = Cart.objects.filter(user=request.user, purchased=False)
                    for item in cart_items:
                        item.purchased = True
                        item.save()
                    print('Order Submited Successfully')
                    return redirect('store_app:index')


                
                #ssl commerz
                if pay_method.payment_method == 'SSLcommerz':
                    store_id = settings.STORE_ID
                    print("==============*****============")
                    print(store_id)
                    print("==============*****============")
                    store_pass = settings.STORE_PASS
                    print("==============*****============")
                    print(store_pass)
                    print("==============*****============")

                    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_pass)

                    print("==============***1**============")
                    print(mypayment)
                    print("==============*****============")
                    
                    status_url = request.build_absolute_uri(reverse('status'))


                    print("==============***2**============")
                    print(status_url)
                    print("==============*****============")

                    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

                

                    order_qs = Order.objects.filter(user=request.user, ordered=False)
                    order_items = order_qs[0].orderitems.all()
                    order_item_count = order_qs[0].orderitems.count()
                    order_total = order_qs[0].get_totals()

                    print("==============***3**============")
                    print(order_qs)
                    print(order_items)
                    print(order_item_count)
                    print(order_total)
                    print("==============***3**============")

                    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='clothing', product_name=order_items, num_of_item=order_item_count, shipping_method='Courier', product_profile='None')

                    current_user = request.user

                    print(current_user)
                    print(current_user.profile.full_name)
                    print(current_user.email)
                    print(current_user.profile.address)
                    print(current_user.profile.city)
                    print(current_user.profile.zipcode)
                    print(current_user.profile.country)
                    print(current_user.profile.phone)



                    billing_address = BillingAddress.objects.filter(user=request.user) [0]

                    mypayment.set_customer_info(name=billing_address.first_name, email=current_user.email, address1=billing_address.address1, address2=billing_address.address2, city=billing_address.city, postcode=billing_address.zipcode, country=billing_address.country, phone=billing_address.phone_number)

                    
                    mypayment.set_shipping_info(shipping_to=billing_address.address1, address=billing_address.address2, city=billing_address.city, postcode=billing_address.zipcode, country=billing_address.country)


                    

                    
                    response_data = mypayment.init_payment()

                    print("==============***4**============")
                    print(response_data['status'])
                    # print(response_data['sessionkey'])
                    # print(response_data['GatewayPageURL'])
                    # print(response_data['failedreason'])
                    print("==============***4**============")

                    print("==========================")
                    print(response_data)
                    print("==========================")
                    
                    return redirect(response_data['GatewayPageURL'])

                return redirect('checkout')

            else:
                return redirect('store_app:index')

        else:
            return redirect('store_app:index')


@csrf_exempt
def sslc_status(request):
    if request.method == 'post' or request.method == 'POST':
        payment_data = request.POST
        # print("=============*****=============")
        # print(payment_data)
        # print("==============*****============")
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request, "Payment Successfully!")
            return HttpResponseRedirect(reverse('sslc_complete', kwargs = {'val_id': val_id, 'tran_id': tran_id}))

        else:
            messages.warning(request, "Payment Unsuccessfully!")
            return redirect('order_app:cart')
    
    return render(request, 'store_app/status.html')


def sslc_complete(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    order.ordered = True
    order.orderId = val_id
    order.paymentId = tran_id
    order.save()
    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()
    return redirect('store_app:index')