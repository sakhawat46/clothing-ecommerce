from django.shortcuts import render
from contact_app.models import Contract
from store_app.models import Product

# Create your views here.

def contact(request):

    contact_details = Contract.objects.order_by('mobile')




    if request.method == 'post' or request.method == 'POST':
        search_product = request.POST.get('search_product')
        products = Product.objects.filter(name__icontains=search_product).order_by('-id')
        context = {
            'products' : products
            }
        return render(request, 'store_app/search.html', context)



    context ={'contact_details': contact_details}
    return render(request,'contact_app/contact.html', context)