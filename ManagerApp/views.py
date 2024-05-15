from django.shortcuts import render

def home(request):
    # Render the index.html template
    return render(request, 'index.html')

def about(request):
    # Render the about.html template
    return render(request, 'about.html')

def contact(request):
    # Render the about.html template
    return render(request, 'contact.html')


# views.py

from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Task.objects.create(text=text)
            return redirect('home')
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
    except Task.DoesNotExist:
        pass
    return redirect('home')
