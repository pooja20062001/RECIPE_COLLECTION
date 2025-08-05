from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the title',
                'size': 50
            }),
            'ingredients': forms.Textarea(),
            'instructions': forms.Textarea(),
            'preparation_time': forms.TimeInput(attrs={
                'type': 'time'
            }),
        }


        
        

        