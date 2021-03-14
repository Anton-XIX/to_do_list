from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import filters
from .models import ToDoList
from .serializers import ToDoListSerializer, SingleToDoListSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class ToDoListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']
    filters.SearchFilter.search_description = 'Type task name '


class SingleToDoListView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = ToDoList.objects.all()
    serializer_class = SingleToDoListSerializer


class ToDoListCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
