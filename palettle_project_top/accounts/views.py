from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, palettes
from .forms import ProfileForm, PaletteForm

# Profile view
class ProfileView(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        # Get the user profile and user's palettes
        context = super().get_context_data(**kwargs)
        user_profile = self.object
        user_palettes = palettes.objects.filter(user=user_profile.user)

        colors = []
        for palette in user_palettes:
            # Append colors and palette primary key to the context
            colors.append([palette.color_1, palette.color_2, palette.color_3, palette.color_4, palette.color_5, palette.pk])

        context['palettes'] = colors
        context['form'] = PaletteForm()
        return context

    def post(self, request, *args, **kwargs):
        # Handle POST request when adding a new palette
        user_profile = self.get_object()
        form = PaletteForm(request.POST)
        if form.is_valid():
            # Save the new palette and associate it with the user
            palette = form.save()
            palette.user = user_profile.user
            palette.save()
            return redirect('profile-page', pk=user_profile.pk)
        else:
            # If form is not valid, render the form with errors
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

# Delete palette view
class DeletePaletteView(View):
    def post(self, request, pk, *args, **kwargs):
        # Handle POST request to delete a palette
        palette = palettes.objects.get(pk=pk)
        palette.delete()
        return redirect('profile-page', pk=palette.user.profile.pk)

# Sign up view
class signupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'

    # No additional methods or overrides

# Profile redirect view
def profileRedirectView(request):
    # Redirect to the user's profile page if it exists
    user = request.user
    if hasattr(user, 'profile'):
        return redirect('profile-page', pk=user.pk)

# Random palette view
class RandomPaletteView(View):
    def get(self, request):
        # Render the random.html template
        return render(request, 'random.html')

# Home page view
class HomePageView(View):
    def get(self, request):
        # Render the homepage.html template
        return render(request, 'homepage.html')
