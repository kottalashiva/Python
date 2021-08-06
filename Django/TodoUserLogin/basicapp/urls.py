from django.contrib import admin
from django.urls import path, re_path
from basicapp import views
from django.contrib.auth.views import LogoutView

app_name = 'basicapp'
urlpatterns = [
    path('create_task/', views.CreateTaskView.as_view(), name="create_task"),
    path('tasks_list/', views.TaskView.as_view(), name="task_list"),
    re_path('delete/(?P<pk>[0-9]+)$', views.DeleteTaskView.as_view(), name="delete_task"),
    re_path('update/(?P<pk>[0-9]+)$', views.UpdateTaskView.as_view(), name="update_task"),
    path('logout/', views.UserLogOut.as_view(), name='logout'),
    path('', views.UserLoginView.as_view(), name="login_view"),

]
