from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django import forms
from pethub.forms import UserForm, UserProfileForm
from django.shortcuts import redirect
# Create your views here.

@login_required
def index(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/index.html')
    #Get response for client and return it (updating cookies if need be) 
    return response

def about_us(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/about-us.html')
    #Get response for client and return it (updating cookies if need be) 
    return response

def trending(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/trending.html')
    #Get response for client and return it (updating cookies if need be) 
    return response

def extra_information(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/extra-information.html')
    #Get response for client and return it (updating cookies if need be) 
    return response

def species(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/species.html')
    #Get response for client and return it (updating cookies if need be) 
    return response

def user_login(request):
    # boolean to show success of registration
    registered = False
    user_form = UserForm()
    profile_form = UserProfileForm()
    
    #Try and get data if POST method used
    if request.method == "POST":

        # for users that wish to register
        if request.POST.get('submit') == "Register":
            # fill in data from UserForm and UserProfileForm
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                # save user info to the database
                user = user_form.save()

                # hash password for user object
                user.set_password(user.password)
                user.save()
                
                #Sort out UserProfile instance, setting commit to false for the moment to avoid integrity issues
                profile = profile_form.save(commit=False)
                profile.user = user

                #If a profile picture is provided, save it to the UserProfile model
                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                # save UserProfile instance
                profile.save()

                # show registration was successful
                registered = True
            else:
                # form was invalid, print error message
                print(user_form.errors, profile_form.errors)

        # for users that want to be signed in instead
        elif request.POST.get('submit') == "Log in":
            username = request.POST.get('username')
            password = request.POST.get('password')

            #authenticate username and password
            user = authenticate(username=username,password=password)

            # If credentials are valid
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    # Account is disabled, so user cannot log in
                    return HttpResponse("Your account is disabled.")
            else:
                print("Invalid login details: {0}, {1}".format(username, password))
                return HttpResponse("Invalid login details - please try again.")

    ####################################################################################
    # May need to edit to suit both forms        
       
    else:
        #not using POST methods, so make new models 
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    #Render template according to data received
    return render(request, 'pethub/login.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,
                       'registered': registered})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
