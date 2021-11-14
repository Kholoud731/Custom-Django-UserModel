from django.contrib import admin
from django.urls import path
from .views import signup,logout
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('signup/', signup, name='signup'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # login auth returns token
    path('logout/', logout, name='logout'),

]




