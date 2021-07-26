from django.conf.urls import url
from basicapp import views


urlpatterns = [
    url("forms/", views.form_name_view, name="form_name_view"),
    url('', views.index, name='index'),

]
