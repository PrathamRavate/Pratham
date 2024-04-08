from leaves.models import Leave
from profiles.models import Profile
from rest_framework import serializers


class LeaveSerializer(serializers.Serializer):
    leave_type = serializers.CharField(max_length=50)
    employee = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    startdate = serializers.DateField()
    enddate = serializers.DateField()
    status = serializers.ChoiceField(choices=Leave.STATUS)

    def create(self, validated_data):
        return Leave.objects.create(**validated_data)


