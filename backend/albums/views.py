from rest_framework import permissions, generics, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import QueryDict
from .serializers import AlbumSerializer, TrackCreateSerializer
from .models import Album, Track

class AlbumAPI(generics.GenericAPIView):
    serializer_class = AlbumSerializer
    permissons_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (
            {
                'album' : serializer.data
            }
        )

class AlbumDetailAPI(generics.GenericAPIView):
    serializer_class = AlbumSerializer
    querset = Album.objects.all()


class AlbumTrackAPI(generics.GenericAPIView):
    # queryset = Track.objects.objects.all()
    serializers = TrackCreateSerializer
    
    def post(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({serializer.data})