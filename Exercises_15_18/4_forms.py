# forms.py

from django import forms
from .models import Human

class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'surname', 'date_birth', 'place_residence']
