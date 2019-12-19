from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff == False:
                return render(request, "accounts/login.html", {'not_staff': True})
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
    return redirect('articles:list')


def requests(request):
    users = User.objects.filter(is_staff=False)
    return render(request, "accounts/requests.html", {'users': users})


def accept(request, user):
    user = User.objects.get(username=user)
    user.is_staff = True
    user.save()
    return redirect("accounts:requests")
