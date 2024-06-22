from rest_framework import viewsets
from .serializer import ProductsSerializer
from . models import products

# Create your views here.

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = ProductsSerializer