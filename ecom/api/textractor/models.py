from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
class AnimationObject(models.Model):
    name = models.CharField(max_length=50)
    similar_keywords = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # After creating your model, register it in admin.py
    
    # Make a str constructor
    def __str__(self):
        return self.name
    
# Model for animated objects
class temp_anims(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    similar_keywords = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Make a str constructor
    def __str__(self):
        return self.name