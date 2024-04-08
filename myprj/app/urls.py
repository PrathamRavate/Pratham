from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_todos),  
    path('todos/', views.get_todos, name='get_todos'),
    path('todos/<uuid:uid>/', views.get_todo_detail, name='get_todo_detail'),
    path('todos/create/', views.create_todo, name='create_todo'),
    path('todos/<uuid:uid>/update/', views.update_todo, name='update_todo'),
    path('todos/<uuid:uid>/delete/', views.delete_todo, name='delete_todo'),
]
