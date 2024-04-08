from django.shortcuts import render
from leaves.models import Leave
from rest_framework import status
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LeaveSerializer

@api_view(['GET'])
def leave_week(request):
    leaves = Leave.objects.filter(startdate__range=["2024-04-01", "2024-04-30"])
    serializer = LeaveSerializer(leaves, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def leave_currentweek(request):
    current_datetime = timezone.now()
    current_week = current_datetime.isocalendar()[1]

    leaves = Leave.objects.filter(startdate__week=current_week, status="APPROVED")
    serializer = LeaveSerializer(leaves, many=True)
    return Response(serializer.data)


from django.http import JsonResponse
from datetime import datetime
from .models import Leave



