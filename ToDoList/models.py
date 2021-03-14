from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ToDoList(models.Model):
    name = models.CharField(max_length=100, verbose_name='Task name')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    perform_date = models.DateTimeField()
    is_performed = models.BooleanField(default=False, verbose_name='Task status')

    def __str__(self):
        return f'{self.name} - {self.user}'
