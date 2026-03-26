from django.urls import path
from . import views
urlpatterns = [
    path('', views.posts_list),
    path('update/', views.update_page),
    path("about/", views.AboutPage.as_view())
]