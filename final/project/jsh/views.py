from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserProfileUpdateForm, UserEmailUpdateForm
from .models import UserProfile, Customer

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a Customer profile for the new user
            customer = Customer(user=user, email=user.email)
            customer.save()

            login(request, user)
            print("User registered and logged in successfully.")
            return redirect('dashboard')
        else:
            print("Form is not valid. Errors:", form.errors)  # Add this line to see form errors
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})


def update_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        email_form = UserEmailUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, instance=user_profile)

        if email_form.is_valid() and profile_form.is_valid():
            email_form.save()
            profile_form.save()
            return redirect('dashboard')
    else:
        email_form = UserEmailUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=user_profile)

    return render(request, 'update_profile.html', {'email_form': email_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
