from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/<int:user_id>', views.delete_user),
    path('create_user', views.create_user)
]
