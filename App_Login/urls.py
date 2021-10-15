from django.urls import path
from . import views

app_name = 'Login_App'

urlpatterns = [
    path('login/', views.log_in, name='login')
]
