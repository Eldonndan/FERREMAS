from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ferremas.forms import CustomUserCreationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'cliente':
                    return redirect('cliente_dashboard')
                elif user.user_type == 'vendedor':
                    return redirect('vendedor_dashboard')
                elif user.user_type == 'bodeguero':
                    return redirect('bodeguero_dashboard')
                elif user.user_type == 'contador':
                    return redirect('contador_dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def cliente_dashboard(request):
    return render(request, 'cliente_dashboard.html')

def vendedor_dashboard(request):
    return render(request, 'vendedor_dashboard.html')

def bodeguero_dashboard(request):
    return render(request, 'bodeguero_dashboard.html')

def contador_dashboard(request):
    return render(request, 'contador_dashboard.html')