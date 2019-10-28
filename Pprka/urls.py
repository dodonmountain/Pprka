from django.contrib import admin
from django.urls import path, include
from indexes import urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('indexes.urls')),
    path('payments/', include('payments.urls')),
    path('accounts/', include('accounts.urls')),
<<<<<<< HEAD
    path('products/', include('products.urls')),
=======
    path('accounts/', include('allauth.urls')), 
>>>>>>> 2b0856c75b6438c6a35ced8011ad095cff1e3850
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
