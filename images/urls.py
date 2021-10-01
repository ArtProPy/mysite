""" URL config image """
from django.urls import path

from images import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id_image>/<slug:slug>/', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
]