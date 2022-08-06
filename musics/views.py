import re
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer
from .models import Music
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def musics_list(request):
  if request.method == 'GET':
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    serializer = MusicSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   
@api_view(['GET','PUT','DELETE'])
def musics_detail(request,pk):
  music = get_object_or_404(Music, pk=pk)
  if request.method == 'GET':
    serializer=MusicSerializer(music)
    return(Response(serializer.data, status=status.HTTP_200_OK))
    
  elif request.method == 'PUT':
    serializer = MusicSerializer(music, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return(Response(serializer.data, status=status.HTTP_200_OK))
  elif request.method == 'DELETE':
    music.delete()
    return(Response(status=status.HTTP_404_NOT_FOUND))


    #   {
    #     "id": 4,
    #     "title": "Donence",
    #     "artist": "Baris Manco",
    #     "album": "Sozum Meclisten Disari",
    #     "release_date": "1981-07-01",
    #     "genre": "Anatolian Rock"
    # }