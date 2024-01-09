from django.shortcuts import render

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# import model
from django.contrib.auth import get_user_model

# import serializer
from .serializer import UserAccountCreateSerializer

# permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# authentication
from django.contrib.auth import authenticate, login, logout


class UserAcountCreateView(CreateAPIView):
    model = get_user_model
    serializer_class = UserAccountCreateSerializer


class UserLoginView(CreateAPIView):
    serializer_class = UserAccountCreateSerializer

    # override the post method for our login logic
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        print("username , password :::::: ", email, password)

        '''
         it checks our user's email and passwords are valid or not
        '''
        user_data = authenticate(email=email, password=password)

        ''' 
        if it is valid it will create JWT's Refresh and Access Token for the user
        '''
        if user_data:
            refresh = RefreshToken.for_user(user_data)
            access_token = refresh.access_token
            user_serializer = UserAccountCreateSerializer(user_data)
            # returns http method 200
            return Response({'Message': 'login success', "refresh_token": str(refresh), "access_token": str(access_token)}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'Login Failed, Check Email & Password'}, status=status.HTTP_401_UNAUTHORIZED)


# logout
class UserLogoutView(APIView):
    '''
    implemented auth and permissions class for restricting invalid users,
    it will allow only if they gave an essesntial credential
    '''
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh_token")
        print(refresh_token)

        if refresh_token:
            delete_token = RefreshToken(refresh_token)
            delete_token.blacklist()
            return Response({"Message": "Logout sucess"}, status=status.HTTP_200_OK)
        else:
            print(refresh_token, "error")
            return Response({"Message": "Logout Failed,chekc the given credentials"}, status=status.HTTP_403_FORBIDDEN)
