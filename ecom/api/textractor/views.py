# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimationObjectSerializer
from .models import AnimationObject
# Create your views here.

class AnimationObjectViewSet(viewsets.ModelViewSet):
    # 
    queryset = AnimationObject.objects.all().order_by('name')
    serializer_class = AnimationObjectSerializer
    
    # Now you need to setup the urls