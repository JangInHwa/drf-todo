from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Todo
		fields = '__all__'
	def validate_title(self, value):
		if len(value) > 50:
			raise serializers.ValidationError('Title is too long!')
		return value
