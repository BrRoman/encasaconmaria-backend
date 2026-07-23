from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET', 'POST'])
def products(request):
    items = Product.objects.all()
    items_serialized = ProductSerializer(items, many=True)
    return Response(items_serialized.data, status=status.HTTP_200_OK)
