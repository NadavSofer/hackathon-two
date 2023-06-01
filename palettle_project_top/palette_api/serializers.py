from rest_framework import serializers
from .models import Palette

class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = ['pk','color_1','color_2', 'color_3', 'color_4', 'color_5']


