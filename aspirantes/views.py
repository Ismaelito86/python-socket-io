from django.shortcuts import render
from .serializers import AspiranteSerializer
from .models import Aspirante
from rest_framework import viewsets

# Create your views here.
class IsmaViewSet(viewsets.ModelViewSet):
    queryset = Aspirante.objects.all()
    serializer_class = AspiranteSerializer
    #permission_classes = []