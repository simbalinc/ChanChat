from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse


User = get_user_model()


@login_required(login_url='/log_in/')
def user_list(request):
    # TODO Never to be done in production
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'instant/user_list.html', {'users': users})


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


@login_required(login_url='/log_in/')
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


