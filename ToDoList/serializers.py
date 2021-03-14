from rest_framework import serializers
from .models import ToDoList
from django.contrib.auth import get_user_model

User = get_user_model()


class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = ToDoList
        fields = ('user', 'name', 'perform_date', 'is_performed')


class SingleToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('name', 'perform_date', 'is_performed')
