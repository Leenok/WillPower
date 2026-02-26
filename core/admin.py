from django.contrib import admin
from .models import Workout, Exercise, WorkoutExercise

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'workout_type', 'duration')
    list_filter = ('workout_type', 'date', 'user')
    search_fields = ('title', 'notes')
    date_hierarchy = 'date'

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscle_group')
    list_filter = ('muscle_group',)
    search_fields = ('name',)

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'sets', 'reps', 'weight')
    list_filter = ('workout__user',)

