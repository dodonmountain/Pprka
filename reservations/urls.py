from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', view.index, name='index'),
    
]