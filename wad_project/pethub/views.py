from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django import forms
from pethub.forms import UserForm, UserProfileForm, PostForm, UpdateUserForm, UpdateUserProfileForm
from django.shortcuts import redirect
from pethub.models import UserProfile, User, Post, Comment
# Create your views here.

@login_required
def index(request):
    post_list = Post.objects.order_by('-upload_date')
    
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/index.html', {'post_list' : post_list})
    #Get response for client and return it (updating cookies if need be) 
    return response

@login_required
def about_us(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/about-us.html')
    #Get response for client and return it (updating cookies if need be) 
    return response

@login_required
def trending(request):
    post_list = Post.objects.order_by('-likes')
    
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/trending.html', {'post_list' : post_list})
    #Get response for client and return it (updating cookies if need be) 
    return response

@login_required
def extra_information(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/extra-information.html')
    #Get response for client and return it (updating cookies if need be) 
    return response

@login_required
def species(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/species.html')
    #Get response for client and return it (updating cookies if need be) 
    return response

@login_required
def user_profile(request, username):
    # create context dictionary holding user's name
    user = User.objects.get(username=username)
    userProfile = UserProfile.objects.get_or_create(user=user)[0]

    context_dict = {'user' : user,
                    'userProfile' : userProfile}
    return render(request, 'pethub/user.html', context_dict)

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
                if 'userPicture' in request.FILES:
                    profile.userPicture = request.FILES['userPicture']

                # save UserProfile instance
                profile.save()

                # show registration was successful
                registered = True
                login(request, user)
                return redirect(reverse('index'))
        
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
                    return redirect(reverse('index'))
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

@login_required
def post_upload(request):
    # boolean to show success of upload
    uploaded = False


    #Try and get data if POST method used
    if request.method == "POST":
        # fill in data from UserForm and UserProfileForm
            post_form = PostForm(data=request.POST)
            

            if post_form.is_valid():
                # save user info to the database
                post = post_form.save(commit=False)

                # save associated user
                post.user = request.user

                # Save post information
                post.save()

                #save many-to-many relationship for tags
                post_form.save_m2m()

                #If a post picture is provided, save it to the UserProfile model
                if 'picture' in request.FILES:
                    post.picture = request.FILES['picture']
                
                # save post instance
                post.save()

                # show registration was successful
                uploaded = True
                
            else:
                # form was invalid, print error message
                print(post_form.errors, post_form.errors)

    else:
        #not using POST methods, so make new models 
        post_form = PostForm()
        
    
    context_dict = {'post_form': post_form,
                       'uploaded': uploaded,}
    #Render template according to data received
    return render(request, 'pethub/post-upload.html', context_dict)
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

#view for updating user profile
@login_required
def update_user(request):
    updated = False
    user = request.user
    profile = UserProfile.objects.get(user=user)

    #If a post, make new forms for updating old objects
    if request.method == 'POST':
        update_user_profile_form = UpdateUserProfileForm(request.POST, instance=profile)
        update_user_form = UpdateUserForm(request.POST, instance=user)

        # Check both forms are valid
        if update_user_form.is_valid() and update_user_profile_form.is_valid():
            
            #update user model with new information and save it
            user = update_user_form.save()
            user.set_password(user.password)
            user.save()

            # Update associated profile for user and save
            profile = update_user_profile_form.save(commit=False)
            profile.save()

            #change picture if a new one is uploaded
            if 'userPicture' in request.FILES:
                profile.userPicture = request.FILES['userPicture']
            else:
                profile.userPicture = None
                
            profile.save()

            updated = True
            login(request, user)
            
        else:
            # form was invalid, print error message
            print(user_form.errors, profile_form.errors)
    else:
        update_user_form = UpdateUserForm()
        update_user_profile_form = UpdateUserProfileForm
        
    return render(request, 'pethub/update-user.html', {'update_user_profile_form' : update_user_profile_form,
                                                       'update_user_form': update_user_form,
                                                       'updated': updated})
    


