from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class TodoApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    task_description = models.CharField(max_length=500)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('basicapp:task_list')
