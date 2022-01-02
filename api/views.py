from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Artist
from .serializers import ArtistSerializer

# Create your views here.

class ArtistAPI (APIView):
    
    def get (self, req):
        
        model = Artist.objects.all()
        
        serializer = ArtistSerializer(model, many=True)
        
        return Response(serializer.data)
    
    def post (self, req):
        
        serializer = ArtistSerializer(data = req.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)