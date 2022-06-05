from django.urls import path
from . import views

urlpatterns = [
    path('', views.populate, name='index'),
    path('search/', views.weapon_search, name='search'),
]