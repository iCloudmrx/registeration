from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .form import LoginForm

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse("Disabled login")
            else:
                return HttpResponse("Invalid login")
        else:
            form = LoginForm()
    return render(request, 'account/login.html', {'form': form})