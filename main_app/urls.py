from django.urls import path
from . import views

# name ='home' is a kwarg

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # PROJECTS
    path('projects/', views.ProjectList.as_view(), name='projects_index'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='detail'),
    # TASKS
    path('tasks/', views.task_list, name='task_list')
    # COMMENTS
    # REGISTRATION
    path('accounts/signup/', views.signup, name='signup'),

]