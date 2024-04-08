from events.models import Event
from rest_framework import serializers

class EventSerializer:
    def is_timesheet_filed(employee_id):
      
        start_date = "2024-04-01"
        end_date = "2024-04-30"

        events_exist = Event.objects.filter(employee_id=employee_id, date__range=[start_date, end_date]).exists()
        return events_exist

class TimesheetStatusSerializer(serializers.Serializer):
    timesheet_status = serializers.CharField()


class EventSerializers(serializers.Serializer):
    starttime = serializers.DateTimeField()
    endtime = serializers.DateTimeField()
    employee_id = serializers.IntegerField()
    project_id = serializers.IntegerField()
    status = serializers.CharField(max_length=50)

