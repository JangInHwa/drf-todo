from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = '__all__'

	def update(self, instance:Todo, validated_data):
		instance.is_done = validated_data('is_done')
		instance.save()
		return instance
