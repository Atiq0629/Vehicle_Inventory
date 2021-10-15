from django.urls import path
from . import views

app_name = 'Vehicle_App'

urlpatterns = [
    path('', views.dashboard, name='home')

]