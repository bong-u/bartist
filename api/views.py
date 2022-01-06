from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Artist
from .serializers import ArtistSerializer

# Create your views here.

class ArtistAPI (APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    
    def get (self, req):
        queryset = Artist.objects.all()
        # model = Artist.objects.all()
        
        # serializer = ArtistSerializer(model, many=True)
        
        # return Response(serializer.data)def index(request):

        # context = {
        #     'artist': model
        # }
        
        return Response( {'artist': queryset} )
        # return render(req, 'index.html')
        
    
    def post (self, req):
        
        serializer = ArtistSerializer(data = req.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)