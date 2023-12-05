
from django import forms
from anillos.models import anillo

class AnilloForm(forms.ModelForm):
    class Meta:
        model = anillo
        fields = '__all__'
