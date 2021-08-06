from django.shortcuts import render
from basicapp import models
from django.http import HttpResponse
from basicapp.forms import TasksForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView

#Shiva
#hello@123

#skottala
#Welcome123

# Create your views here.
def index(request):
    return HttpResponse("<h1> Hi from the Index </h1>")

class UserLoginView(LoginView):
    fields = "__all__"
    template_name = "basicapp/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('basicapp:task_list')

class UserLogOut(LogoutView):
    template_name = "basicapp/logout.html"
    def get_success_url(self):
        return reverse_lazy('basicapp:login_view')

class MainMenu(TemplateView):
    template_name = "basicapp/base_page.html"

class TaskView(LoginRequiredMixin, ListView):
    model = models.TodoApp
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        return context

class CreateTaskView(CreateView):
    model = models.TodoApp
    fields = ("task", "task_description")
    # form = TodoAppForm()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)

class DeleteTaskView(DeleteView):
    model = models.TodoApp
    success_url = reverse_lazy('basicapp:task_list')

class UpdateTaskView(LoginRequiredMixin,UpdateView):
    model = models.TodoApp
    fields = ("task", "task_description")

    def get_success_url(self):
        return reverse_lazy('basicapp:task_list')
