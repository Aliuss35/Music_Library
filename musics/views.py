from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer
from .models import Music


@api_view(['GET','POST'])
def musics_list(request):
  if request.method == 'GET':
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=TRUE)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = MusicSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   
@api_view(['GET'])
def musics_detail(request,pk):
  music = Music.objects.get(pk=pk)
  return(Response(pk))