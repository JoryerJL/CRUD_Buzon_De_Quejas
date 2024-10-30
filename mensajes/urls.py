from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mensajes_list, name='list'),
    path('delete/<int:pk>/', mensajes_delete, name='delete'),
    path('create/', mensajes_create, name='create'),
    path('actualizar/<int:pk>/', mensajes_update, name='update'),
]