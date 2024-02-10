from itertools import product
from multiprocessing import context
from pyexpat import model
from re import search
from unicodedata import category, name
from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
from store_app.models import Category, Product, ProductImages, Banner

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

# def home(request):
#     return render(request, 'store_app/index-4.html')


class HomeListView(TemplateView):
    def get(self, request, *args, **kwargs):

        products = Product.objects.all().order_by('-id')
        
        print(products)
        banners = Banner.objects.filter(is_active=True).order_by('-id')[0:5]
        categorys = Category.objects.all().order_by('-id')
        print("///////////////11111111111///////////////////")
        print(categorys)
        print("//////////////////////////////////")

        context = {
            'products' : products,
            'banners' : banners,
            'categorys' : categorys
        }
        return render(request, 'store_app/index-4.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            search_product = request.POST.get('search_product')
            products = Product.objects.filter(name__icontains=search_product).order_by('-id')
            context = {
                'products' : products
                }
            return render(request, 'store_app/search.html', context)




class ShopListView(TemplateView):
    def get(self, request, *args, **kwargs):

        products = Product.objects.all().order_by('-id')
        paginator = Paginator(products,4)
        page = request.GET.get('page')

        print(products)
        banners = Banner.objects.filter(is_active=True).order_by('-id')[0:5]
        categorys = Category.objects.all().order_by('-id')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'products' : products,
            'banners' : banners,
            'categorys' : categorys
        }
        return render(request, 'store_app/shop.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            search_product = request.POST.get('search_product')
            products = Product.objects.filter(name__icontains=search_product).order_by('-id')
            context = {
                'products' : products
                }
            return render(request, 'store_app/search.html', context)





    # model = Product
    # template_name = 'store_app/index-4.html'
    # context_object_name = "products"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['banners'] = Banner.objects.filter(is_active=True).order_by('-id')[0:5]
    #     return context


# def product_details(request, pk):
#     item = Product.objects.get(id=pk)
#     context = {
#         'item': item
#     }
#     return render (request, 'store_app/product.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store_app/product.html'
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        return context



    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            search_product = request.POST.get('search_product')
            products = Product.objects.filter(name__icontains=search_product).order_by('-id')
            context = {
                'products' : products
                }
            return render(request, 'store_app/search.html', context)


# class CategorieDetailView(DetailView):
#     model = Category
#     template_name = 'store_app/category.html'
    
#     context_object_name = "category"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(product)
#         return context



def category_details(request, slug):
    category = Category.objects.get(slug=slug)
    product = Product.objects.filter(category=category)





    if request.method == 'post' or request.method == 'POST':
        search_product = request.POST.get('search_product')
        products = Product.objects.filter(name__icontains=search_product).order_by('-id')
        context = {
            'products' : products
            }
        return render(request, 'store_app/search.html', context)





    print("/////////////////222222222222/////////////////")
    print(category)
    print("//////////////////////////////////")
    print(product)
    context = {
        'category': category,
        'product' : product
    }
    return render (request, 'store_app/category.html', context)
