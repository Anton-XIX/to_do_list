from django.urls import path

from .views import ToDoListView, SingleToDoListView, ToDoListCreateView

urlpatterns = [
    path('to-do-list/list', ToDoListView.as_view()),
    path('to-do-list/single_action/<str:pk>', SingleToDoListView.as_view(), name='url-create'),
    path('to-do-list/create', ToDoListCreateView.as_view()),

]
