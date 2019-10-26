from django.contrib import admin
from django.urls import path, include
from indexes import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('indexes.urls'))
]
