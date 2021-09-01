from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from todo.serializers import TodoSerializer
from .models import Todo
from rest_framework.views import APIView
from rest_framework.request import HttpRequest

class TodoView(APIView):
	def get(self, request:HttpRequest):
		todos = Todo.objects.all()
		serializer = TodoSerializer(todos, many = True)
		return Response(serializer.data)
	def post(self, request:HttpRequest):
		serializer = TodoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

class TodoDetailView(APIView):
	def get(self, request:HttpRequest, pk:int):
		todo = get_object_or_404(Todo, pk=pk)
		serializer = TodoSerializer(todo)
		return Response(serializer.data)
	
	def put(self, request:HttpRequest, pk:int):
		todo = get_object_or_404(Todo, pk=pk)
		serializer = TodoSerializer(instance=todo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

	def delete(self, request:HttpRequest, pk:int):
		todo = get_object_or_404(Todo, pk = pk)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
@api_view(['GET', 'POST'])
def todos(request:HttpRequest):
	if request.method == 'GET':
		queryset = Todo.objects.all()
		serializer = TodoSerializer(queryset, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = TodoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request:HttpRequest, pk):
	if request.method == 'GET':
		todo = get_object_or_404(Todo, pk=pk)
		serializer = TodoSerializer(todo)
		return Response(serializer.data)
	elif request.method == 'PUT':
		todo = get_object_or_404(Todo, pk=pk)
		serializer = TodoSerializer(instance=todo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)
	elif request.method == 'DELETE':
		todo = get_object_or_404(Todo, pk=pk)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
