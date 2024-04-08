from django.urls import path
from .views import check_timesheet_status
from .views import check_timesheet_view_req
from .views import check_timesheet_view

urlpatterns = [
  
    path('check-timesheet_req/<int:employee_id>/', check_timesheet_status, name='check_timesheet_status'),
     path('check-timesheet/<int:employee_id>/', check_timesheet_view_req, name='check_timesheet'),
     path('check-timesheet_edit/<int:employee_id>/', check_timesheet_view, name='check_timesheet'),
]

    




