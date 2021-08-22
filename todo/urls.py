from django.contrib import admin
from django.urls import path, include
from .views import todo_detail, todos

urlpatterns = [
	path('todos/', todos),
    path('todos/<int:pk>', todo_detail)
]
