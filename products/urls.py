from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:product_pk>/', views.detail, name='detail'),
    path('<int:product_pk>/create/', views.comment_create, name='comment_create'),
    path('<int:product_pk>/create/basket/', views.basket_create, name='basket_create'),
    path('<int:user_pk>/basket/', views.basket, name='basket'),
]