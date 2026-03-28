from . import views
from django.urls import path 
urlpatterns = [
    path('', views.news),
    path('update/', views.update),
    path('tournament/', views.tournament)
]

