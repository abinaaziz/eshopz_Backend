from django.urls import path

from .views import (
    RegisterView,
    MyTokenObtainPairView,
    MyProfileView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('profile/', MyProfileView.as_view(), name='profile'),
]