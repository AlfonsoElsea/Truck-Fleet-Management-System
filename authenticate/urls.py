from django.urls import path
from mysqlx import Auth

from .views import logoutUser, register_user,login_user


urlpatterns = [
    path('login_user', login_user,name='login'),
    path('register', register_user,name='register'),
    path('logout', logoutUser,name='logout'),

    

]   