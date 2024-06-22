from rest_framework import serializers
from .models import usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'