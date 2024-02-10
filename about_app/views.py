from django.shortcuts import render
from about_app.models import About
from store_app.models import Product

# Create your views here.

def about(request):
    about_information = About.objects.order_by('at_a_glance')



    if request.method == 'post' or request.method == 'POST':
        search_product = request.POST.get('search_product')
        products = Product.objects.filter(name__icontains=search_product).order_by('-id')
        context = {
            'products' : products
            }
        return render(request, 'store_app/search.html', context)



    context ={'about_information': about_information}
    return render(request,'about_app/about.html', context)