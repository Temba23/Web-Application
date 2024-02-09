from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can login now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your account. Please check the form.')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)
    
@login_required
def view_profile(request):
    u_form=UserUpdateForm(instance=request.user)
    p_form=ProfileUpdateForm(instance=request.user.profile)
    context = {
        "u_form" : u_form,
        "p_form" : p_form
    }
    return render(request, "user/view_profile.html", context)
    




def forgot_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your Password Is Changed.")
            return redirect('blog-home')
        else:
            messages.error(request, "Error While Filling The Form.")
            # Return a response here to handle the case when the form is not valid.
            return render(request, "user/change_password.html", {"form": form})

    else:
        form = PasswordChangeForm(request.user)
        return render(request, "user/change_password.html", {"form": form})