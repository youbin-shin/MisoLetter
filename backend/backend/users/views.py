from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import ProfileSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):

    def retrieve(self, request, pk=None):
        queryset = Profile.get_object_or_404(user_id=pk)
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data)

