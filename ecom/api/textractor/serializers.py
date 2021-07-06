from rest_framework import serializers
from .models import AnimationObject, temp_anims

class AnimationObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimationObject
        fields = ('name','similar_keywords')

class tempAnimSerializer(serializers.HyperlinkedModelSerializer):
    video = serializers.FileField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    class Meta:
        model = temp_anims
        fields = ('name','video', 'similar_keywords')