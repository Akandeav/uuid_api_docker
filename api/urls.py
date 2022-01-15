from django.contrib import admin
from django.urls import path
from .views import UUIDView

urlpatterns = [
    path('uuid', UUIDView.as_view())
]