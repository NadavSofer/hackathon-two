from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, palettes
from .forms import ProfileForm



class profile_view(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.object
        user_palettes = palettes.objects.filter(user=user_profile.user)

        colors = []
        for palette in user_palettes:
            colors.append([palette.color_1, palette.color_2, palette.color_3, palette.color_4, palette.color_5])

        context['palettes'] = colors
        return context


class signup_view(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'

def profile_redirect_view(request):
    user = request.user
    if hasattr(user, 'profile'):
        return redirect('update-profile')

def UpdateProfile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        filled_form = ProfileForm(request.POST, instance=profile) # instance - the instance in the database to update
        if filled_form.is_valid():
            filled_form.save()
            return redirect('posts-all')
        else:
            errors = filled_form.errors
            print(errors)

    form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'profile_update.html', context)


class UpdateProfileView(UpdateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'profile_update.html'
    success_url = 'posts-all'

    def get_object(self):
        return self.request.user.profile