from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'LojaMuseu'

router = routers.DefaultRouter()
router.register('', views.LojaMuseuViewSet, basename='LojaMuseu')

urlpatterns = [
    path('', include(router.urls) )
]