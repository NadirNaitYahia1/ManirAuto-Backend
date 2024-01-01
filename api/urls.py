from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('user/', views.user, name='user'),
    path('logout/', views.logout, name='logout'),
    path('addCar/', views.addCar, name='addCar'),
    path('getCars/', views.getCars, name='getCar'),
    # path('getCar/', views.getCar, name='getCar'),
    path('getCarById/', views.getCarById, name='getCarById'),
    path('getCarByOwner/', views.getCarByOwner, name='getCarByOwner'),
    path('deleteCar/', views.deleteCar, name='deleteCar'),
    path('updateCar/', views.updateCar, name='updateCar'),
    
]
