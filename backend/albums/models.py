from django.db import models 
from django.conf import settings
from Miso.utils import ChoiceEnum

class Album(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover_img = models.CharField(max_length=256)
    background_img = models.CharField(max_length=256)
    title = models.CharField(max_length=100)
    d_day = models.DateTimeField()
    join_count = models.IntegerField()
    created = models.DateTimeField(auto_created=True)


class Track(models.Model):
    class Status(ChoiceEnum):
        DELETE = 0
        ONLY_OWNER = 1
        PUBLIC = 2

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='track')
    nickname = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    audio = models.CharField(max_length=256)
    duration = models.IntegerField()
    seq = models.IntegerField()
    status = models.SmallIntegerField(default=Status.PUBLIC.value, choices=Status.choices())
    created = models.DateTimeField(auto_created=True)

