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
    path('accounts/', include('allauth.urls')),
    # path('products/', include('products.urls')),
    # path('reservations/', include('reservations.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
