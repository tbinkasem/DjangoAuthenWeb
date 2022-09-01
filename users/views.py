from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'คุณได้ลงทะเบียนใช้งานแล้ว ตอนนี้ สามารถเข้าระบบได้แล้ว')
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegistrationForm()

    context = { 'form' : form }
    return render(request, 'users/register.html', context)

