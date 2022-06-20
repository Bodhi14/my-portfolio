from pydoc import describe
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import InfoAPI
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home, name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
