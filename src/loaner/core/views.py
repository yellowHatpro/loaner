from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm
from item.models import User
from .tasks import calculate_user_credit_score


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user)

        context = {
            'user': user
        }
        return render(request, 'core/dashboard.html', context)
    else:
        return render(request, 'core/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print(request)
            # user = User.objects.get(email=request.user)
            # calculate_user_credit_score.delay(user)
            form.save()

            return redirect('/api/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('/api/login/')
