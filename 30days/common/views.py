from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from common.forms import ProfileForm
from django.contrib.auth.decorators import login_required


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('common:addition')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def check(request):
    """
    가입 전 비만검사
    """
    return render(request, 'common/check.html')


@login_required(login_url='common:login')
def addition(request):
    """
    가입 후 기초대사랑, 권장대사량, 자신이 매일 하고자 하는 운동 시간
    """
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('main:index')
    else:
        form = ProfileForm()
        return render(request, 'common/addition.html', {'form': form})
