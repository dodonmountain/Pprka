from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.index, name='index'),
    path('pay/', views.pay, name='pay'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('fail/', views.fail, name='fail'),
]