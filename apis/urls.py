from django.urls import path
from . import views
from .views import RegisterAPI

urlpatterns =[
    path('viewUsers/',views.UserListCreateAPIView.as_view()),   
    path('products/',views.ProductArtListCreateAPIView.as_view()),
    path('orderartview/',views.OrderArtListCreateAPIView.as_view()),
    path('register/', views.RegisterAPI, name='register'),
    path('login/',views.user_login),
    
]







# from .views import  UsersAPI
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('viewUsers',UsersAPI)
# router.register('register',UsersAPI)

# + router.urls