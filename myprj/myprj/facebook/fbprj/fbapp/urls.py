from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_post_details),
    path('posts/', views.get_post_details, name='get_post_details'),
   path('posts/<int:post_id>/', views.get_likes_for_post, name='get_likes_for_post'),
   path('search/', views.search_objects, name='search_objects'),
]
