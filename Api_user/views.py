from rest_framework import viewsets
from .serializer import UserSerializer
from .models import usuario
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UserSerializer
