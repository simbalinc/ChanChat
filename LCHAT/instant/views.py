from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse


def user_list(request):
    return render(request, 'instant/user_list.html')


def log_in(request):
    """
    Form checks if there's a supplied username and password then returns the
    user object.
    We then log in the authenticated user and redirect them to the homepage
    """
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('instant:user_list'))
        else:
            print(form.errors)
    return render(request, 'instant/log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('instant:log_in')


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('instant:log_in'))
        else:
            print(form.errors)
    return render(request, 'instant/sign_up.html', {'form': form})


