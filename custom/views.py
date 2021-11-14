# from django.shortcuts import render
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from .models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
# Create your views here.



@api_view(['GET', 'POST']) # login function 
def signup(request):
    if request.method == 'GET': # made to test the get with the post for the same path
        data_users = User.objects.all()
        users = UserSerializer(data_users,many=True)
        print(users)

        return Response(data=users.data)
    elif request.method == 'POST':
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            users = User.objects.get(id = user.data['id'])
            token= Token.objects.create(user=users)
            print(token.key)
            return Response({'msg':'User Created!', 'token':token.key})
        return Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)  



@api_view(["GET"])  
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout(request):
    print(request.user.auth_token)
    print(request.user.id)
    request.user.auth_token.delete()
    users = User.objects.get(id = request.user.id)
    token= Token.objects.create(user=users)
    print(token.key)
    return Response({'msg': 'Logged out'}, status=status.HTTP_200_OK)
