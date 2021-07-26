from django.shortcuts import render
from basicapp.forms import Form

# Create your views here.
def index(request):
    return render(request, "basicapp/homepage.html")

def form_name_view(request):
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            raise ValidationError("Form contain some errors")
    form_dict = {"form": form}
    return render(request, "basicapp/user.html",form_dict)
