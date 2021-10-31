from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import (UserLoginForm)
from .views import *

app_name = 'account'
# uid - user id
# b64 - type data - byte 64
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/', account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', account_activate, name='activate'),
    # User dashboard
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/edit/', edit_details, name='edit_details'),
]