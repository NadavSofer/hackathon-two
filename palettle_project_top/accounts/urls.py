from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import profile_view, signup_view, profile_redirect_view, UpdateProfile, UpdateProfileView

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('profile/<int:pk>', profile_view.as_view(), name='profile-page'),
    path('signup/', signup_view.as_view(), name='signup'),
    path('update_profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('profile-redirect/', profile_redirect_view, name='profile-redirect'),
]