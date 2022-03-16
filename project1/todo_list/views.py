from django.shortcuts import render
from .models import Task

def main_page(request):
    tasks = Task.objects.all()
    return render(request, 'main_page.html', {'tasks': tasks})