from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def login_page(request):

    if request.method == 'POST':
        usernamenya = request.POST.get('username')
        passwordnya = request.POST.get('password')

        user = authenticate(request, username=usernamenya, password=passwordnya)

        if user is not None:
            login(request, user)
            return redirect('halaman_utama')
        else:
            messages.info(request, 'Username atau Password salah')
            return render(request, 'login_page.html')

    return render(request, 'login_page.html')

def logout_user(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url='login_page')
def halaman_utama(request):
    return render(request, 'main_app/halaman_utama.html')