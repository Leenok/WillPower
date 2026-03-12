# core/views.py
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Workout, WorkoutExercise, Exercise
from .forms import WorkoutForm, WorkoutExerciseForm

def home(request):
    return render(request, 'main/home.html')

# @login_required
# def profile(request):
#     """Страница профиля (только для авторизованных)"""
#     return render(request, 'profile.html', {'user': request.user})



@login_required(login_url='/accounts/login/')
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    return render(request, 'core/workout_list.html', {'workouts': workouts})


@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('add_exercises', workout_id=workout.id)
    else:
        form = WorkoutForm()
    
    return render(request, 'core/add_workout.html', {'form': form})

# @login_required
# def add_exercises(request, workout_id):
#     workout = Workout.objects.get(id=workout_id, user=request.user)
#     exercises = Exercise.objects.all()
    
#     if request.method == 'POST':
#         # Обработка добавления упражнений
#         for key, value in request.POST.items():
#             if key.startswith('exercise_'):
#                 exercise_id = key.replace('exercise_', '')
#                 sets = request.POST.get(f'sets_{exercise_id}')
#                 reps = request.POST.get(f'reps_{exercise_id}')
#                 weight = request.POST.get(f'weight_{exercise_id}')
                
#                 if sets and reps:
#                     WorkoutExercise.objects.create(
#                         workout=workout,
#                         exercise_id=exercise_id,
#                         sets=sets,
#                         reps=reps,
#                         weight=weight or 0
#                     )
#         return redirect('workout_detail', workout_id=workout)
    
#     return render(request, 'core/add_exercises.html', {
#         'workout': workout,
#         'exercises': exercises
#     })


# @login_required
# def profile(request):
#     """Страница профиля (только для авторизованных)"""
#     return render(request, 'profile.html', {'user': request.user})

# @login_required(login_url='/custom-login/')  # Свой URL для входа
# def dashboard(request):
#     """Панель управления"""
#     return render(request, 'dashboard.html')