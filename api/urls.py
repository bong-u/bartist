from django.urls import path
from .views import ArtistAPI

urlpatterns = [
    path('', ArtistAPI.as_view()),
]