from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path('',views.home, name='home'),
    path('products/',views.products,name='products'),
    path('login/',views.login_user,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
] 
