from rest_framework import serializers
from .models import Aspirante


class AspiranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspirante
        fields = '__all__'
    