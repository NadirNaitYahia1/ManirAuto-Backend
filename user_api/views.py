# views.py
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import AppUserSerializer
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    if request.method == 'POST':
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def loginUser(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        print('email',email)
        print('password',password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'User logged in successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logoutUser(request):
    logout(request)
    return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
