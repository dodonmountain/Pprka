from django.urls import path, include
from . import views
app_name = 'indexes'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('index/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
]
