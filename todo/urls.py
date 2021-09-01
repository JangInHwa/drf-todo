from django.urls import path
from .views import TodoView, TodoDetailView

urlpatterns = [
	path('todos/', TodoView.as_view(), name='moview-list'),
    path('todos/<int:pk>', TodoDetailView.as_view(), name='movie-detail'),
]
