from asyncio import Task
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task

class TaskList(ListView):
    # looks for task_list.html
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    # looks for task_detail.html
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    # looks for task_form.html
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    # looks for task_form.html
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
