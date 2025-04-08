from django.urls import path
from . import views

urlpatterns =[
    path('viewUsers/',views.UserListCreateAPIView.as_view()),   
    path('products/',views.ProductArtListCreateAPIView.as_view()),
    path('orderartview/',views.OrderArtListCreateAPIView.as_view())

]





# from .views import  UsersAPI
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('viewUsers',UsersAPI)
# router.register('register',UsersAPI)

# + router.urls