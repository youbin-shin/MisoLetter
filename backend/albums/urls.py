from django.urls import path
from .views import AlbumAPI, AlbumDetailAPI, AlbumTrackAPI

urlpatterns = [
    path('', AlbumAPI.as_view()),
    path('<int:pk>/', AlbumDetailAPI.as_view()),
    path('<int:pk>/track/', AlbumTrackAPI.as_view()),
]   