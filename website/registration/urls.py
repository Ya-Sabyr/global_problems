from django.urls import path
from .views import RegistrationFormView, LoginFormView, ChangePasswordView, LogOutView, ProfileView

urlpatterns = [
    path('', RegistrationFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name ='change-password'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
