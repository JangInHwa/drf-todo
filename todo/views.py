from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .models import Todo
from .serializers import TodoSerializer

class TodoView(APIView):
	def get(self, request:Request):
		todos = Todo.objects.all()
		serializer = TodoSerializer(todos, many = True)
		return Response(serializer.data)
	def post(self, request:Request):
		serializer = TodoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

class TodoDetailView(APIView):
	def get(self, request:Request, pk:int):
		todo = get_object_or_404(Todo, pk=pk)
		serializer = TodoSerializer(todo)
		return Response(serializer.data)
	
	def put(self, request:Request, pk:int):
		todo = get_object_or_404(Todo, pk=pk)
		serializer = TodoSerializer(instance=todo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

	def delete(self, request:Request, pk:int):
		todo = get_object_or_404(Todo, pk = pk)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
@api_view(['GET', 'POST'])
def todos(request:Request):
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
def todo_detail(request:Request, pk):
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
