
from django import forms
from anteojos.models import anteojo

class AnteojoForm(forms.ModelForm):
    class Meta:
        model = anteojo
        fields = '__all__'


