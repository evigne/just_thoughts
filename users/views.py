from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

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

@login_required  # settings.py LOGIN_URL = 'users_login'
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has successfully updated')
            redirect('users_profile')


    elif request.method == 'GET':
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


