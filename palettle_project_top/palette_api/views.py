import json
from rest_framework import generics
from .models import Palette
from .serializers import PaletteSerializer
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# API view for listing and creating palettes
class PaletteList(generics.ListCreateAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer


# API view for retrieving, updating, and deleting a specific palette
class PaletteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer


# View for rendering the form to create a new palette
def Palette_create(request):
    if request.method == 'POST':
        serializer = PaletteSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('Palette-list')
    else:
        serializer = PaletteSerializer()
    return render(request, 'Palette_create.html', {'serializer': serializer})


# View for creating a new palette via POST request (API endpoint)
@csrf_exempt
def Palette_create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = PaletteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Palette created successfully.'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


# View for rendering the form to update an existing palette
def Palette_update(request, pk):
    Palette = Palette.objects.get(pk=pk)
    if request.method == 'POST':
        serializer = PaletteSerializer(instance=Palette, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('Palette-list')
    else:
        serializer = PaletteSerializer(instance=Palette)
    return render(request, 'Palette_update.html', {'serializer': serializer, 'Palette': Palette})


# View for deleting an existing palette
def Palette_delete(request, pk):
    Palette = Palette.objects.get(pk=pk)
    if request.method == 'POST':
        Palette.delete()
        return redirect('Palette-list')
    return render(request, 'Palette_delete.html', {'Palette': Palette})


# View for returning all palettes as JSON response
def palettesOut(request):
    palettes = Palette.objects.all()
    serializer = PaletteSerializer(palettes, many=True)
    return JsonResponse(serializer.data, safe=False)
