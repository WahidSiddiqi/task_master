from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Profile, Task, Comment
#registration imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# HOME




def home(request):
    return render(request, 'home.html')

# ABOUT




def about(request):
    return render(request, 'about.html')

# PROFILE
class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile/detail.html'


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['department']

#TASK VIEWS
class TaskList(ListView):
    model = Task
    template_name = 'tasks/index.html'
# class TaskDetail(DetailView):
#     model = Task
#     template_name = 'tasks/detail.html'

def tasks_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  comments = Comment.objects.filter()
  return render(request, 'tasks/detail.html', {
    'comments': comments, 
    'task': tasks,
  })

class TaskCreate(CreateView):
    model = Task
    # fields = ['title', 'description', 'owner', 'due_date', ' project', 'status', 'priority']
    fields = '__all__'
    success_url = '/tasks/'




class TaskUpdate(UpdateView):
    model = Task
    # fields = ['title', 'description', 'owner', 'due_date', ' project', 'status', 'priority']
    fields = '__all__'
    success_url = '/tasks/'
class TaskDelete(DeleteView):
    model = Task
    # instead of fields or using the absolure_url, we just use a success_url
    success_url = '/tasks/'


# PROJECT VIEWS
class ProjectList(ListView):
    model = Project
    template_name = 'projects/index.html'



# class ProjectDetail(DetailView):
#     model = Project
#     template_name = 'projects/detail.html'

def projects_detail(request, proj_id):
  project = Project.objects.get(id=proj_id)
  tasks = Task.objects.filter()
  print('these are my tasks',tasks)
  return render(request, 'projects/detail.html', {
    # include the cat and feeding_form in the context
    'project': project, 
    'tasks': tasks,
  })


class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'description', 'due_date', 'status']
    success_url = '/projects/'

# UpdateView, very similar to CreateView, needs model and fields


class ProjectUpdate(UpdateView):
    model = Project
    # let's make it so you cant rename a project
    fields = ['title', 'description', 'due_date', 'status']
    success_url = '/projects'


class ProjectDelete(DeleteView):
    model = Project
    # instead of fields or using the absolure_url, we just use a success_url
    success_url = '/projects'


# TASK VIEWS
def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'task_list.html', {'tasks' : tasks})
  
# COMMENT VIEWS

# REGISTRATION VIEWS
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('projects_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)