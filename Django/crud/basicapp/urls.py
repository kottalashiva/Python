from django.conf.urls import url
from basicapp import views

app_name="basicapp"
urlpatterns = [
    url(r"^$", views.SchoolList.as_view(), name="school_list"),
    url(r"^(?P<pk>\d+)/$",views.SchoolDetailView.as_view(), name="detail"),
    url(r"^create/$",views.SchoolCreateView.as_view(), name="create"),
    url(r"update/(?P<pk>\d+)/$",views.SchoolUpdateView.as_view(), name="update"),
    url(r"delete/(?P<pk>\d+)/$",views.SchoolDeleteView.as_view(), name="delete"),
]
