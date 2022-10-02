from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('results', views.ResultView)

urlpatterns = [
   path('', include(routers.urls)),
]
