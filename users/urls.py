from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('profile/', views.profile, name='profile'),
    path('history/', views.history, name='history'),


    path('edit-profile/', views.editProfile, name='edit-profile'),
    path('adress/', views.adress, name='adress'),
    # path('properties/', views.property_list, name='property_list'),
    path('property=<uuid:pk>/', views.mainProperty, name='main-property'),
    path('home/', views.home, name='home'),





]
