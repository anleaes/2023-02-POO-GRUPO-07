from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'exposicoes'

router = routers.DefaultRouter()
router.register('', views.ExposicaoViewSet, basename='exposicoes')

urlpatterns = [
    path('', include(router.urls) )
]