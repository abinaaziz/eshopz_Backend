# from rest_framework import generics
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView

# from .serializers import RegisterSerializer, MyTokenObtainPairSerializer


# class RegisterView(generics.CreateAPIView):

#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]


# class MyTokenObtainPairView(TokenObtainPairView):

#     serializer_class = MyTokenObtainPairSerializer


from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    RegisterSerializer,
    MyTokenObtainPairSerializer,
    ProfileSerializer
)


class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class MyTokenObtainPairView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer


class MyProfileView(generics.RetrieveAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile