from django import forms
from .models import UserProfile, palettes

class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


class PaletteForm(forms.ModelForm):
    class Meta:
        model = palettes
        fields = ['color_1', 'color_2', 'color_3', 'color_4', 'color_5']
