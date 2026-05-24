from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm


@login_required(login_url='login')
def home(request):

    search = request.GET.get('search')

    if search:

        tasks = Task.objects.filter(
            user=request.user,
            title__icontains=search
        ).order_by('-created')

    else:

        tasks = Task.objects.filter(
            user=request.user
        ).order_by('-created')

    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect('home')
        
         # DASHBOARD STATISTICS

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(
        completed=True
    ).count()

    pending_tasks = tasks.filter(
        completed=False
    ).count()

    # PROGRESS PERCENTAGE

    if total_tasks > 0:

        progress = int(
            (completed_tasks / total_tasks) * 100
        )

    else:

        progress = 0
        
    context = {
        'tasks': tasks,
        'form': form,

        'total_tasks': total_tasks,

        'completed_tasks': completed_tasks,

        'pending_tasks': pending_tasks,

        'progress': progress,

    }

    return render(request, 'home.html', context)


def register_user(request):

    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

    return render(request, 'login.html')


def logout_user(request):

    logout(request)

    return redirect('login')


@login_required(login_url='login')
def delete_task(request, pk):

    task = get_object_or_404(
        Task,
        id=pk,
        user=request.user
    )

    task.delete()

    return redirect('home')


@login_required(login_url='login')
def complete_task(request, pk):

    task = get_object_or_404(
        Task,
        id=pk,
        user=request.user
    )

    task.completed = not task.completed

    task.save()

    return redirect('home')


@login_required(login_url='login')
def update_task(request, pk):

    task = get_object_or_404(
        Task,
        id=pk,
        user=request.user
    )

    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():

            form.save()

            return redirect('home')

    context = {
        'form': form
    }

    return render(
        request,
        'update_task.html',
        context
    )