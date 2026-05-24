from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:

        model = Task

        fields = ['title', 'priority', 'due_date']

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter a task...',
                    'class': 'task-input'
                }
            ),

            'priority': forms.Select(
                attrs={
                    'class': 'task-select'
                }
            ),

            'due_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'task-date'
                }
            )

        }