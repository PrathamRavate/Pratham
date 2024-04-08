# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import AuthTokenSerializer
from rest_framework import status

@api_view(['POST'])
def obtain_auth_token(request):
    if request.method == 'POST':
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request=request, username=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
