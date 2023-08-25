from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) #makes the form functional
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #validates the info within the form
            form.save() #saves the user
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')#flash message
            messages.success(request, f"Your acoount has been created! You are now able to log in ")
            # return redirect('blog-home')
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
@login_required #so that user can't go to profile directly through url
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your acoount has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, 'users/profile.html',context)