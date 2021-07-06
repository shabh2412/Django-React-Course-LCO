from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register(r'anim_obj', views.AnimationObjectViewSet, 'animation_objects')
router.register(r'temp_anim', views.tempAnimViewSet, 'temp')

urlpatterns = [
    path('', include(router.urls))
]