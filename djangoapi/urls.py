from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Hello, world!
    path('', views.index, name='index')
]
