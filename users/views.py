from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome to JustThoughts {username}, you can now login')
            return redirect('users_login')



    elif request.method == 'GET':
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

# Create your views here.
