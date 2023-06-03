from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView, signupView, profileRedirectView, DeletePaletteView, HomePageView, RandomPaletteView

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile-page'),
    path('signup/', signupView.as_view(), name='signup'),
    path('profile-redirect/', profileRedirectView, name='profile-redirect'),
    path('delete-palette/<int:pk>/', DeletePaletteView.as_view(), name='delete-palette'),
    path('random_palette/', RandomPaletteView.as_view(), name='randomPalette'),
    path('homepage/', HomePageView.as_view(), name='homepage'),
]