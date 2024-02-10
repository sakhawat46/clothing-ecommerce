from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('fashion_app.urls')),
    path('', include('store_app.urls')),
    path('order/', include('order_app.urls')),
    path('payment/', include('payment_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('about/', include('about_app.urls')),
    path('contact/', include('contact_app.urls')),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)