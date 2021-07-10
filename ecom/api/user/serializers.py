from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes
# Decorators allows you to write or add some things into those pre-written things remotely.