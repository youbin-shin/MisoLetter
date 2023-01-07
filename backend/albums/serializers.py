from rest_framework import serializers
from .models import Album, Track


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        field = '__all__'
    

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        field = '__all__'


class TrackCreateSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(required=False)
    title = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)
    seq = serializers.IntegerField(required=True)
    status = serializers.IntegerField(required=False)

    def validate(self, data):
        # nickname 설정
        # album 설정
        # album = Album.objects.get(pk=pk)

        if data.get('status') in Track.Status.get_values():
            raise serializers.ValidationError()
        if data.get('seq') > 10:
            raise serializers.ValidationError()
        