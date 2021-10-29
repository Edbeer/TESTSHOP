from django.urls import path
from .views import *

app_name = 'account'
# uid - user id
# b64 - type data - byte 64
urlpatterns = [
    path('register/', account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', account_activate, name='activate')
]