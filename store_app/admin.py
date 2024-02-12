from pyexpat import model
from django.contrib import admin
from store_app.models import Category, Product, ProductImages, VariationValue, Banner, MyLogo, MyFavicon
# Register your models here.


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)




class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


# admin.site.register(VariationValue)
admin.site.register(Banner)
# admin.site.register(MyLogo)
# admin.site.register(MyFavicon)

