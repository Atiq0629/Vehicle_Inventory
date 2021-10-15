from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('Vehicle_App:home'))
        else:
            messages.error(request, 'Invalid Username or Password!')
    return render(request, 'Login_App/login.html')



# def log_in(request):
#     form = AuthenticationForm
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('Vehicle_App:home'))
#     return render(request, 'Login_App/login.html', context={'form': form})
