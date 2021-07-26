from django.shortcuts import render
from django.http import HttpResponse
from basicapp.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return HttpResponse("<h1>hello this is from index</h1>")

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    dict = {"user_form": user_form, "profile_form": profile_form, "registered": registered}
    return render(request, "basicapp/register.html", dict)
