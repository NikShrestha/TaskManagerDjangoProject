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

from django.shortcuts import render, redirect
from .models import Profile

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            # Check if the username already exists
            if Profile.objects.filter(signup_username=username).exists():
                return render(request, 'signup.html', {'error_message': 'Username already exists'})
            else:
                # Create a new Profile instance and save signup credentials
                profile = Profile(signup_username=username)
                profile.save_signup_credentials(username, password1)
                return redirect('signin')  # Redirect to signin page after successful signup
        else:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})
    return render(request, 'signup.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Profile

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            profile = Profile.objects.get(signup_username=username)
            if profile.signup_password == password:  # Check password
                user = authenticate(request, username=username, password=password)
                if user is not None:  # Authenticate user
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'signin.html', {'error_message': 'Authentication failed'})
            else:
                return render(request, 'signin.html', {'error_message': 'Invalid username or password'})
        except Profile.DoesNotExist:
            return render(request, 'signin.html', {'error_message': 'User not registered'})
    return render(request, 'signin.html')
