# core/forms.py
from django import forms
from .models import Workout, WorkoutExercise, Exercise

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'workout_type', 'date', 'start_time', 'duration', 
                  'calories_burned', 'feeling', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'duration': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class WorkoutExerciseForm(forms.ModelForm):
    """Базовая форма для добавления упражнения в тренировку"""
    
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'duration', 'distance', 'notes', 'order']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Заметки к упражнению...'}),
            'sets': forms.NumberInput(attrs={'min': 1, 'max': 100, 'class': 'form-control'}),
            'reps': forms.TextInput(attrs={'placeholder': 'например: 12, 10, 8'}),
            'weight': forms.NumberInput(attrs={'step': '0.5', 'min': 0, 'class': 'form-control'}),
            'duration': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'step': '0.1', 'min': 0, 'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }
        labels = {
            'exercise': 'Упражнение',
            'sets': 'Количество подходов',
            'reps': 'Повторения',
            'weight': 'Вес (кг)',
            'duration': 'Длительность',
            'distance': 'Дистанция (км)',
            'notes': 'Заметки',
            'order': 'Порядок выполнения',
        }
        help_texts = {
            'reps': 'Укажите повторения для каждого подхода через запятую',
            'duration': 'Для кардио-упражнений',
        }
