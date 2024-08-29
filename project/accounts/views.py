from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import FormView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CustomUserCreationForm, CustomPasswordChangeForm

class PasswordChangeView(FormView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('accounts:password_changed')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return HttpResponseRedirect(self.get_success_url())
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html', {'user': request.user})

class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
