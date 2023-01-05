from rest_framework import permissions, generics, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.models import AuthToken
from django.http import QueryDict
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer
from .models import User


class SignupAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response (
            {
                'user' : CreateUserSerializer(
                    user, context = self.get_serializer_context()
                ).data,
                'token': token,
            }
        )

class SigninAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                'user': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                'token': AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def get(self, request, nickname):
        user = User.objects.get(nickname=nickname)
        serializer = UserSerializer(user)
        return Response(serializer.data)