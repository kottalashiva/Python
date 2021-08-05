from django.shortcuts import render
from basicapp import models
from django.http import HttpResponse
from basicapp.forms import TasksForm
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView


# Create your views here.
def index(request):
    return HttpResponse("<h1> Hi from the Index </h1>")

class MainMenu(TemplateView):
    template_name = "basicapp/base_page.html"


class TaskView(ListView):
    model = models.Tasks

class CreateTaskView(CreateView):
    model = models.Tasks
    fields = ("taskid", "task_name", "task_description")
    # form = TasksForm()

class DeleteTaskView(DeleteView):
    model = models.Tasks
    success_url = reverse_lazy('basicapp:task_list')

class UpdateTaskView(UpdateView):
    model = models.Tasks
    fields = ("task_name", "task_description")

    def get_success_url(self):
        return reverse_lazy('basicapp:task_list')
