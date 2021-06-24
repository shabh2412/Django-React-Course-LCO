from rest_framework import serializers
from .models import AnimationObject

class AnimationObjectSerializer(serializers.Serializer):
    class Meta:
        model = AnimationObject
        field = ('name','similar_keywords')