from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, palettes
from .forms import ProfileForm, PaletteForm



class ProfileView(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.object
        user_palettes = palettes.objects.filter(user=user_profile.user)

        colors = []
        for palette in user_palettes:
            colors.append([palette.color_1, palette.color_2, palette.color_3, palette.color_4, palette.color_5, palette.pk])

        context['palettes'] = colors
        context['form'] = PaletteForm()
        return context


    def post(self, request, *args, **kwargs):
        user_profile = self.get_object()
        form = PaletteForm(request.POST)
        if form.is_valid():
            palette = form.save()
            palette.user = user_profile.user
            palette.save()
            return redirect('profile-page', pk=user_profile.pk)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class DeletePaletteView(View):
    def post(self, request, pk, *args, **kwargs):
        palette = palettes.objects.get(pk=pk)
        palette.delete()
        return redirect('profile-page', pk=palette.user.profile.pk)


class signupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'


def profileRedirectView(request):
    user = request.user
    if hasattr(user, 'profile'):
        return redirect('profile-page', pk=user.pk)


# class RandomPaletteView(DetailView):
#     model = UserProfile
#     template_name = 'random.html'
#     context_object_name = 'profile'


class RandomPaletteView(View):
    def get(self, request):
        return render(request, 'random.html')


class HomePageView(View):
    def get(self, request):
        return render(request, 'homepage.html')
