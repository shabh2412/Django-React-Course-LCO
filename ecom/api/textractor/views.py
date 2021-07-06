# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimationObjectSerializer, tempAnimSerializer
from .models import AnimationObject, temp_anims
# Create your views here.

class AnimationObjectViewSet(viewsets.ModelViewSet):
    # 
    queryset = AnimationObject.objects.all().order_by('name')
    serializer_class = AnimationObjectSerializer
    
    # Now you need to setup the urls

# View for temp anims
class tempAnimViewSet(viewsets.ModelViewSet):
    queryset = temp_anims.objects.all().order_by('name')
    serializer_class = tempAnimSerializer