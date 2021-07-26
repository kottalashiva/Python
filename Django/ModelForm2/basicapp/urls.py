from django.conf.urls import url
from basicapp import views

urlpatterns = [
    url(r'user', views.form_name_view, name='form_name_view'),
    url(r'^$', views.index, name='index'),
]
