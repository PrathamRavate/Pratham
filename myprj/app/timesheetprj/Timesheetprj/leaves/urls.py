from django.urls import path
from . import views 

urlpatterns = [
    path('leave-week/', views.leave_week, name='leave-week'),
    path('leave-currentweek/', views.leave_currentweek, name='leave-currentweek'),  
]
