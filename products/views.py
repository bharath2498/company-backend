from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "products_list"

        cached_data = cache.get(cache_key)

        if cached_data is not None:
            print("CACHE HIT")
            return Response(cached_data)

        print("CACHE MISS")

        response = super().list(request, *args, **kwargs)

        cache.set(cache_key, response.data, 60)

        return response
