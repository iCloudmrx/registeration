from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .form import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile

from django.contrib.auth.decorators import login_required

# Create your views here.


def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse("Disabled login")
#             else:
#                 return HttpResponse("Invalid login")

#     form = LoginForm()
#     return render(request, 'account/login.html', {'form': form, })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html',
                          {
                              'user': new_user
                          })
    form = UserRegistrationForm()
    return (request, 'account/register.html', {
        'form': form
    })


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,
                             'Profile updated'
                             'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
