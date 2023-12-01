from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)