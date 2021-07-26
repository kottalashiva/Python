from django.shortcuts import render
from django.http import HttpResponse
from basicapp.models  import School, Student
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1> hello World </h1>")

class TemplateEx(TemplateView):
    template_name = "basicapp/template.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["inject_data"] = "I am injected text"
        return context_data

class SchoolList(ListView):
    model = School
    template_name = "basicapp/school_list.html"

class SchoolDetailView(DetailView):
    model = School
    context_object_name = "school_details"

class SchoolCreateView(CreateView):
    model = School
    fields = ("name", "principal", "location")


class SchoolUpdateView(UpdateView):
    model = School
    fields = ("name", "principal")

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("basicapp:school_list")
