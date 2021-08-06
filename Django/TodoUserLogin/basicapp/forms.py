from django import forms
from basicapp.models import TodoApp

class TasksForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = "__all__"
