from django import forms
from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'status', 'deadline_date', 'detailed_description']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Описание задачи'}),
            'status': forms.Select(),
            'deadline_date': forms.DateInput(attrs={'type': 'date'}),
            'detailed_description': forms.Textarea(attrs={'placeholder': 'Подробное описание задачи', 'rows': 3}),
        }
