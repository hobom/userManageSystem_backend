from django.contrib import admin
from django.urls import path

from user.views import TestView, JwtTestView, LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('test', TestView.as_view(), name='test'),
    path('jwt_test', JwtTestView.as_view(), name='jwt_test'),
]
