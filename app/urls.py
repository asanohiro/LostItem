# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_lost_item, name='upload_lost_item'),
    path('map/', views.map_view, name='map_view'),
]
