from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm, ChangePasswordForm
from django.http import HttpResponseRedirect

class RegistrationFormView(FormView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginFormView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True    

    def get_success_url(self):
        return reverse_lazy('home')


class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/changepassword.html'
    success_url = reverse_lazy('login')
    form_class = ChangePasswordForm
    

class LogOutView(TemplateView):
    template_name = 'registration/logout.html'
    
    def get(self, request, *args, **kwargs):
        # Handle GET requests to display the logout confirmation page
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle POST requests to log out the user
        logout(request)
        return HttpResponseRedirect(reverse_lazy('login'))
    

class ProfileView(TemplateView):
    pass