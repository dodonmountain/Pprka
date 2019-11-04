from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.index, name='index'),
    path('select_room/', views.select_room, name='select_room'),
    path('non_member/', views.non_member, name='non_member'),
]