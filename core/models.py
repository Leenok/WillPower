# core/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Workout(models.Model):
    """Модель тренировки"""
    
    # Типы тренировок (можно расширять)
    WORKOUT_TYPES = [
        ('strength', 'Силовая'),
        ('cardio', 'Кардио'),
        ('hiit', 'HIIT'),
        ('yoga', 'Йога'),
        ('crossfit', 'Кроссфит'),
        ('running', 'Бег'),
        ('swimming', 'Плавание'),
        ('cycling', 'Велосипед'),
        ('other', 'Другое'),
    ]
    
    # Основные поля
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField('Название', max_length=200)
    workout_type = models.CharField('Тип тренировки', max_length=20, choices=WORKOUT_TYPES)
    date = models.DateField('Дата тренировки', default=timezone.now)
    start_time = models.TimeField('Время начала', blank=True, null=True)
    duration = models.DurationField('Длительность', help_text='Например: 01:30:00')
    
    # Дополнительная информация
    calories_burned = models.PositiveIntegerField('Сожжено калорий', blank=True, null=True)
    notes = models.TextField('Заметки', blank=True)
    feeling = models.PositiveSmallIntegerField(
        'Самочувствие', 
        choices=[(i, i) for i in range(1, 6)],
        help_text='Оценка от 1 до 5',
        blank=True, null=True
    )
    
    # Метаданные
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    
    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'
        ordering = ['-date', '-start_time']
    
    def __str__(self):
        return f"{self.title} - {self.date}"

# core/models.py
class Exercise(models.Model):
    """Модель упражнения (справочник)"""
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    
    # Категории упражнений
    MUSCLE_GROUPS = [
        ('chest', 'Грудные'),
        ('back', 'Спина'),
        ('legs', 'Ноги'),
        ('shoulders', 'Плечи'),
        ('biceps', 'Бицепс'),
        ('triceps', 'Трицепс'),
        ('abs', 'Пресс'),
        ('cardio', 'Кардио'),
        ('full_body', 'Все тело'),
    ]
    
    muscle_group = models.CharField('Группа мышц', max_length=20, choices=MUSCLE_GROUPS)
    
    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'
    
    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    """Модель упражнения в тренировке"""
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    
    # Порядок выполнения
    order = models.PositiveSmallIntegerField('Порядок', default=1)
    
    # Параметры выполнения
    sets = models.PositiveSmallIntegerField('Подходы')
    reps = models.CharField('Повторения', max_length=50, 
                           help_text='Например: 12, 10, 8 или до отказа')
    weight = models.DecimalField('Вес (кг)', max_digits=5, decimal_places=1, 
                                 blank=True, null=True)
    
    # Длительность для кардио/времени
    duration = models.DurationField('Длительность', blank=True, null=True)
    distance = models.DecimalField('Дистанция (км)', max_digits=5, decimal_places=2,
                                   blank=True, null=True)
    
    notes = models.CharField('Заметки к подходу', max_length=200, blank=True)
    
    class Meta:
        verbose_name = 'Упражнение в тренировке'
        verbose_name_plural = 'Упражнения в тренировке'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.exercise.name} - {self.sets}x{self.reps}"