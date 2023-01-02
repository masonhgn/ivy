from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets
from django.contrib import messages


# for REST API #####

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

####################
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})



@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
    
    
    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileEditForm(instance=request.user.profile)
    context = {
        'user': request.user,
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'account/profile.html', context)




    '''
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile updated successfully.')
        else:
            messages.error(request,'Error updating profile.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form': user_form,'profile_form': profile_form})
    '''


'''
def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(request,username=cd['username'],password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('jobs:homepage')
            else:
                return HttpResponse('Disabled account.')
        else:
            return HttpResponse('Invalid login.')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})
'''



# Create your views here.
