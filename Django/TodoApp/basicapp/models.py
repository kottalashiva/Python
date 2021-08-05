from django.db import models
from django.urls import reverse


# Create your models here.
class Tasks(models.Model):
    taskid = models.IntegerField()
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=250)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse("basicapp:index", kwargs={"pk":self.pk})
