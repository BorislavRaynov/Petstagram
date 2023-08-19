from django.urls import path
from petstagram.photos import views

urlpatterns = [
    path('add/', views.photo_add, name='photo-add'),
    path('<int:pk>/', views.photo_details, name='photo-details'),
    path('edit/<int:pk>/', views.photo_edit, name='photo-edit'),
    path('delete/<int:pk>/', views.photo_delete, name='photo-delete'),
]
