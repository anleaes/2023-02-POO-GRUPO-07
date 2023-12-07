from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'obrasDeArte'

router = routers.DefaultRouter()
router.register('', views.ObraDeArteViewSet, basename='obraDeArte')

urlpatterns = [
    path('', include(router.urls) )
]