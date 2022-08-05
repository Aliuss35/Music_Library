from pickle import TRUE
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer
from .models import Music


@api_view(['GET'])
def musics_list(request):
  musics = Music.objects.all()
  serializer = MusicSerializer(musics, many=TRUE)
  
  return Response(serializer.data)