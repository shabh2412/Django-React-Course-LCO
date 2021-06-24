from rest_framework import serializers
from .models import AnimationObject

class AnimationObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimationObject
        fields = ('name','similar_keywords')