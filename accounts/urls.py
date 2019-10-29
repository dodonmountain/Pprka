from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('', views.my_page, name="my_page"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('update/', views.update, name="update"),
    path('password/', views.update_password, name="update_password"),
]