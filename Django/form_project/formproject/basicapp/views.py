from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Enter /forms to view the form")

def form_name_view(request):
    from basicapp import forms
    # return HttpResponse()
    form = forms.Form()
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            print("Fname is "+ form.cleaned_data["fname"])
            print("Lname is "+ form.cleaned_data["lname"])
            print("Email is "+ form.cleaned_data["email"])
    forms = {"form": form}
    return render(request, "basicapp/form.html",context=forms)
