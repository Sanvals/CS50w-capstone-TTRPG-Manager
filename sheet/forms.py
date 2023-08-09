from django import forms
from .models import Character

class CharacterForm(forms.Form):
    # Info forms
    name = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Character's name",
        })
    )
    
    race_choice = forms.ChoiceField(
        choices = Character.RACE_CHOICES,
        widget = forms.Select(attrs={
            "class": "form-select form-select-sm",
        })
    )
    
    class_choice = forms.ChoiceField(
        choices = Character.CLASS_CHOICES,
        widget = forms.Select(attrs={
            "class": "form-select form-select-sm",
            "id": "id_class_choice"
            })
    )
    
    level = forms.IntegerField(
        widget = forms.NumberInput(attrs={
            "class": "form-control form-group",
            "id": "id_level",
            "value": 1,
        })
    )

    image = forms.URLField(
        required=False,
        widget = forms.URLInput(attrs={
            "class": "form-control form-group",
            "id": "id_image",
            "Placeholder": "Image URL"
        })
    )
    
    alignment = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Alignment",
        })
    )

    background = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Background",
        })
    )

    hp = forms.IntegerField(
        widget = forms.NumberInput(attrs={
            "class": "form-control form-group",
            "id": "id_hp",
            "value": 1,
        })
    )