from django.contrib import admin
# Importing category model
from .models import AnimationObject, temp_anims

# Register your models here.
admin.site.register(AnimationObject)
admin.site.register(temp_anims)