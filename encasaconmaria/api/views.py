from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        items = Product.objects.all()
        filter = request.query_params.get('filter')
        if filter:
            items = items.filter(category__name=filter)
        items_serialized = ProductSerializer(items, many=True)
        return Response(
            items_serialized.data,
            status=status.HTTP_200_OK,
        )
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
