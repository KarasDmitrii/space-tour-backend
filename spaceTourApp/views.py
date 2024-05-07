from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def menu_items(request):
    data = MenuItem.objects.all()
    serializer = MenuItemSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def advantages(request):
    data = Advantage.objects.all()
    serializer = AdvantageSerializer(data, many=True)
    return Response(serializer.data)
