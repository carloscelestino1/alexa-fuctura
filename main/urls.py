from django.urls import path

from . import views

urlpatterns = [
    path('', views.eventoList, name='evento-list'),
    path('evento/<int:id>', views.eventoView, name="evento-view"),
    path('newevento/', views.newEvento, name="new-evento"),
    path('edit/<int:id>', views.editEvento, name="edit-evento"),
    path('delete/<int:id>', views.deleteEvento, name="delete-evento"),
  
]