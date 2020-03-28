from django.contrib import messages
from django.contrib import auth

from django.shortcuts import render, redirect

from .forms import *



def Home(request):
    return render(request, 'index.html')

def profile(request):
    if request.method== 'POST':
        form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
        return redirect('/home/')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    context = {
            'p_form': form
        }
    return render(request, 'profile.html', context)


def HomeView(request):
    quirysets = Profile.objects.get_or_create(user=request.user)
    return render(request, 'home.html', {'quirysets': quirysets})

def Login(request):
    return request(request, "registration/login.html")

def LogOut(request):
    auth.logout(request)
    return render(request, 'registration/logout.html')
