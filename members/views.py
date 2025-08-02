from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from cmsapp.models import *
from .forms import CreateUserProfile, UpdateUserProfile
from django.contrib import messages
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required








                # Author Profile

def profile(request, pk):
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    user_profile = UserProfile.objects.get(profile_id=pk)
    context = {'profile':user_profile, 'categories':categories, 'posts':posts}
    return render (request, 'profile/user_profile.html', context)




                        # Author create profile view

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = CreateUserProfile(request.POST, request.FILES)
        if form.is_valid():
            # Associate the UserProfile with the current user
            profile = form.save(commit=False)
            profile.user = request.user  # Assign the current user
            profile.save()
            messages.info(request, 'Your profile has been created successfully.')
            return redirect('user_account')
    else:
        form = CreateUserProfile()
        categories = Category.objects.all()
        posts = Post.objects.all().order_by('-date_created')
    return render(request, 'profile/create_profile.html', {'form': form, 'categories':categories, 'posts':posts})





                # Update Author Profile

def update_userprofile(request):
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    profile =  request.user.userprofile
    form = UpdateUserProfile(instance = profile)
    if request.method ==  'POST':
        form = UpdateUserProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your profile has been updated.')
            return redirect ('user_account')

    context = {'form':form, 'categories':categories, 'posts':posts}





    return render (request, 'profile/update_profile.html', context)









    









                    # User Account

def user_account(request):
    account = request.user.userprofile
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    context ={'account':account, 'categories':categories, 'posts':posts}

    return render(request, 'profile/user_account.html', context)





                # DeleteView for User Account

def delete_useraccount(request):
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    profile =  request.user.userprofile
    form = UpdateUserProfile(instance=profile)
    if request.method == 'POST':
        profile.delete()
        user = request.user
        user.delete()
        return redirect ('index')
    context = {'form':form, 'categories':categories, 'posts':posts}

    return render (request, 'profile/delete_useraccount.html', context)









                            # AUTHENTICATION


    # Registration

class Registration (generic.CreateView):
    
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy ('login')


    # LogOut

def logout_view(request):
    logout(request)
    return redirect ('login')