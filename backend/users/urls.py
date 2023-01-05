from django.urls import path
from .views import SignupAPI, SigninAPI, UserAPI

urlpatterns = [
    path('signup/', SignupAPI.as_view()),
    path('signin/', SigninAPI.as_view()),
    path('<str:nickname>/', UserAPI.as_view()),
]   