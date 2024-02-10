from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    context = {}
    return render(request, "accounts/register-page.html", context)


def login_view(request):
    context = {}
    return render(request, "accounts/login-page.html", context)


def logout_view(request):
    logout(request)
    return redirect('home')

def show_profile(request, pk):
    context = {}
    return render(request, "accounts/profile-details-page.html", context)


def edit_profile(request, pk):
    context = {}
    return render(request, "accounts/profile-edit-page.html", context)


def delete_profile(request, pk):
    context = {}
    return render(request, "accounts/profile-delete-page.html", context)

