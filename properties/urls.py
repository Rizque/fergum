from django.urls import path
from . import views

urlpatterns = [
    path('add-property/', views.addProperty, name='add-property'),

    path('update-property/<str:pk>/',
         views.updateProperty, name='update-property'),
    path('delete-property/<str:pk>/',
         views.deletePropertry, name='delete-property'),
]
