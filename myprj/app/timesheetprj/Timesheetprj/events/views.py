from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import EventSerializer
from .models import Event
from .serializer import TimesheetStatusSerializer

@api_view(['GET'])
def check_timesheet_view_req(request, employee_id):
    start_date = "2024-04-01"
    end_date = "2024-04-30"
    events_exist = Event.objects.filter(employee_id=employee_id, date__range=[start_date, end_date]).exists()
    data = {'timesheet_filed': events_exist}
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def check_timesheet_status(request, employee_id):
    events_exist = Event.objects.filter(employee_id=employee_id).exists()
    
    if not events_exist:
        timesheet_status = "Employee did not fill the timesheet"
    else:
        events_not_approved = Event.objects.filter(employee_id=employee_id, status='REGISTERED').exists()
        
        if events_not_approved:
            timesheet_status = "Employee filled the timesheet but not approved"
        else:
            events_rejected = Event.objects.filter(employee_id=employee_id, status='REJECTED').exists()
            if events_rejected:
                timesheet_status = "Timesheet is rejected"
            else:
                timesheet_status = "Timesheet is approved"

    serializer = TimesheetStatusSerializer({'timesheet_status': timesheet_status})
    return Response(serializer.data)



@api_view(['GET'])
def check_timesheet_view(request, employee_id):
    start_date = request.data.get('start_date')
    end_date = request.data.get('end_date')
    if not start_date or not end_date:
        return Response({'error': 'Enter start_date and end_date'}, status=status.HTTP_400_BAD_REQUEST)
    events_exist = Event.objects.filter(employee_id=employee_id, date__range=[start_date, end_date]).exists()
    timesheet_filed = events_exist
    
    data = {'timesheet_filed': timesheet_filed}
    return Response(data, status=status.HTTP_200_OK)
