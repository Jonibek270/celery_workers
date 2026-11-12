from django.urls import path
from .views import register_view,verify_otp_view
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', register_view, name='register'),
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('verify/', verify_otp_view, name='verify_otp'),
]
