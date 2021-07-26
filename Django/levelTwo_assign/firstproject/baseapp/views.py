from django.shortcuts import render
from django.http import HttpResponse
from baseapp.models import User

# Create your views here.
def hello(request):
    # return HttpResponse("<h1> Hi this from Views</h1>")
    dict = {"hello": "hello"}
    return render(request, 'baseapp/homepage.html')

def index(request):
    # return HttpResponse("Hi this is from hello")
    uname_list = User.objects.order_by("fname")
    my_dict = {'user_list': uname_list}
    return render(request, "baseapp/user.html", context=my_dict)
