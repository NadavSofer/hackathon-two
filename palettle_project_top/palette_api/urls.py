from django.urls import path
from .views import PaletteList, PaletteDetail, Palette_create, Palette_update, Palette_delete, Palette_create_post

urlpatterns = [
    path('palettes/', PaletteList.as_view(), name='palette-list'),
    path('palettes/<int:pk>/', PaletteDetail.as_view(), name='palette-detail'),
    # path('palettes/create/', PaletteList.as_view(), name='Palette-create'),
    path('palettes/create-post-api/', Palette_create, name='palette-create-post'),
    path('palettes/create-post/', Palette_create_post, name='palette-create'),
    path('palettes/update/<int:pk>/', Palette_update, name='palette-update'),
    path('palettes/delete/<int:pk>/', Palette_delete, name='palette-delete')
]