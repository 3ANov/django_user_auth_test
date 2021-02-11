from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from django_registration.backends.activation.views import RegistrationView

from accounts.forms import CustomUserCreationForm

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', RegistrationView.as_view(success_url='/', form_class=CustomUserCreationForm,
                                               template_name='registration/registration_form.html',
                                               email_subject_template='registration/activation_email_subject.txt'),
         name='django_registration_register'),

]