from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'compradores'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='compradores')

urlpatterns = [
    path('', include(router.urls) )
]