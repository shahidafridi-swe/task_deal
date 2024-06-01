from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
        widgets = {
            'description' : forms.Textarea(attrs={'rows':4}),
            'categories' : forms.CheckboxSelectMultiple
            
        }
        