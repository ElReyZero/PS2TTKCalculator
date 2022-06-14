from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.weapon_search, name='search'),
    path('pushdb/', views.push_db, name='push_db'),
]