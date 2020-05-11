from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages as msgs
from .forms import UserRegisterForm
from .models import Musician

posts = [
    {
        'musician': 'Steve S',
        'title': 'Profile Post 1',
        'content': 'First post',
        'date_posted': 'May 3rd, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'account/home.html', context)


# Decorator to check if user is logged in before displaying profile
@login_required
def profile(request):
    user_id = request.user.id
    musician = Musician.objects.get(id=user_id)
    context = {
        'title': 'Profile',
        'musician': musician
    }
    return render(request, 'account/profile.html', context)


# Decorator to check if user is logged in before displaying profile
@login_required
def messages(request):
    return render(request, 'account/messages.html', {'title': 'Messages'})


# Decorator to check if user is logged in before displaying profile
@login_required
def matches(request):
    return render(request, 'account/matches.html', {'title': 'Matches'})


# Decorator to check if user is logged in before displaying profile
@login_required
def create_ad(request):
    return render(request, 'account/create_ad.html', {'title': 'Create Ad'})


def register(request):
    # Check if the registration form request is a POST request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Verify registration form has valid input
        if form.is_valid():
            # Adds user to django admin page
            form.save()
            username = form.cleaned_data.get('username')
            msgs.success(request, f"Account created for {username}")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})