from asyncio import Task
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
