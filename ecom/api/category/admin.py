from django.contrib import admin
# Importing category model
from .models import Category

# Register your models here.
admin.site.register(Category)