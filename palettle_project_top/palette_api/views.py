import json
from rest_framework import generics
from .models import Palette
from .serializers import PaletteSerializer
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class PaletteList(generics.ListCreateAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer

class PaletteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer

# @csrf_exempt
def Palette_create(request):
    if request.method == 'POST':
        serializer = PaletteSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('Palette-list')
    else:
        serializer = PaletteSerializer()
    return render(request, 'Palette_create.html', {'serializer': serializer})

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

def Palette_delete(request, pk):
    Palette = Palette.objects.get(pk=pk)
    if request.method == 'POST':
        Palette.delete()
        return redirect('Palette-list')
    return render(request, 'Palette_delete.html', {'Palette': Palette})