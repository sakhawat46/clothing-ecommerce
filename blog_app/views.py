from django.shortcuts import render
from blog_app.models import Blog
from store_app.models import Product

# Create your views here.

def blog(request):
    blog_details = Blog.objects.order_by('blog_title')

    if request.method == 'post' or request.method == 'POST':
        search_product = request.POST.get('search_product')
        products = Product.objects.filter(name__icontains=search_product).order_by('-id')
        context = {
            'products' : products
            }
        return render(request, 'store_app/search.html', context)


    context = {'blog_details': blog_details}
    return render(request, 'blog_app/blog.html', context)