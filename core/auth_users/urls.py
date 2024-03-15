from django.urls import  path
from auth_users.views import auth_login

urlpatterns = [
    path('login', auth_login, name='auth_login')
]