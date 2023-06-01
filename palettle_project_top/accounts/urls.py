from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView, signupView, profileRedirectView, UpdateProfile, UpdateProfileView

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile-page'),
    path('signup/', signupView.as_view(), name='signup'),
    path('update_profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('profile-redirect/', profileRedirectView, name='profile-redirect'),
]