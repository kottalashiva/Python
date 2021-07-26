from django.conf.urls import url
from baseapp import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]
