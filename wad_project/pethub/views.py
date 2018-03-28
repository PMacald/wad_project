from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django import forms
from pethub.forms import UserForm, UserProfileForm, PostForm, UpdateUserForm, UpdateUserProfileForm, CommentForm
from django.shortcuts import redirect
from pethub.models import UserProfile, User, Post, Comment
# Create your views here.

@login_required
def index(request):
    #get list of posts
    posts = Post.objects.order_by('-upload_date')
    
    #check if there is a more efficient way to do this
    post_list = paginate(posts, request)
    post_list = set_likes(post_list)
    
    response = render(request, 'pethub/index.html', {'post_list' : post_list,
                                                     'feed_required':True})
    #Get response for client and return it (updating cookies if need be)
    return response

#for setting likes on posts to the number of users that have liked it, rather than an arbritrary number
def set_likes(post_list):
    for post in post_list:
        likes = post.liked_users.count()
        post.likes = likes
        post.save()
    return post_list

#function for splitting up lists of posts and making them into pages for templates
def paginate(posts, request):
    #25 posts per page
    paginator = Paginator(posts,20)

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        #deliver first page
        post_list = paginator.page(1)
    except EmptyPage:
        # if out-of-range, return last page
        post_list = paginator.page(paginator.num_pages)
    return post_list
    

@login_required
def about_us(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/about-us.html')
    #Get response for client and return it (updating cookies if need be)
    return response

@login_required
def trending(request):
    posts = Post.objects.order_by('-likes')
    
    post_list = paginate(posts, request)
    post_list = set_likes(post_list)
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/trending.html', {'post_list' : post_list,
                                                        'feed_required': True})
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
    # create context dictionary holding user's name and posts
    user = User.objects.get(username=username)
    userProfile = UserProfile.objects.get_or_create(user=user)[0]
    userPosts = Post.objects.filter(user=user)
    post_list = paginate(userPosts, request)
    post_list = set_likes(post_list)
    context_dict = {'user' : user,
                    'userProfile' : userProfile,
                    'post_list' : userPosts,
                    'feed_required': True}
    return render(request, 'pethub/user.html', context_dict)

@login_required
def cat(request):
    #Filter object based on tag
    posts = Post.objects.filter(tags__name__in=["cats", "cat", "kitten", "kitty", "feline", "catto", "kitties"]).order_by('-upload_date').distinct()
    post_list = paginate(posts, request)
    post_list = set_likes(post_list)
    response = render(request, 'pethub/cat.html', {'post_list' : post_list,
                                                   'feed_required':True})
    #Get response for client and return it (updating cookies if need be)
    return response

@login_required
def exotic(request):
    #Filter object based on tag
    posts = Post.objects.filter(tags__name__in=["exotic", "lizard", "bird", "lizards", "iguana" "dragon", "fish", "parrot", "birds", "snake", "snakes"]).order_by('-upload_date').distinct()
    post_list = paginate(posts, request)
    post_list = set_likes(post_list)
    response = render(request, 'pethub/exotic-animal.html', {'post_list' : post_list,
                                                             'feed_required':True})
    #Get response for client and return it (updating cookies if need be)
    return response

@login_required
def dog(request):
    #Filter object based on tag
    posts = Post.objects.filter(tags__name__in=["dog", "doggo", "dogs", "puppy", "pup", "pupper"]).order_by('-upload_date').distinct()
    post_list = paginate(posts, request)
    response = render(request, 'pethub/dog.html', {'post_list' : post_list,
                                                   'feed_required':True})
    #Get response for client and return it (updating cookies if need be)
    return response

@login_required
def hutch_animal(request):
    #Filter object based on tag
    posts = Post.objects.filter(tags__name__in=["hutch", "rabbit", "guinea", "hamster", "chinchilla", "guinea-pig", "mice", "mouse", "rabbits", "hamsters", "chinchillas"]).order_by('-upload_date')
    post_list = paginate(posts, request)
    post_list = set_likes(post_list)
    response = render(request, 'pethub/hutch-animal.html', {'post_list' : post_list,
                                                            'feed_required':True})
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
                return render(request, 'pethub/login.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,
                       'registered': registered,
                       'logged_in': False})
                
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

                # show upload was successful
                uploaded = True
                
                return HttpResponseRedirect(reverse('index'))

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
            return user_profile(request,user.username)

        else:
            # form was invalid, print error message
            print(user_form.errors, profile_form.errors)
    else:
        # generate update user forms with pre-populated fields based on their current information
        update_user_form = UpdateUserForm(initial={'username':user.username,'email':user.email, 'first_name':user.first_name, 'last_name':user.last_name})
        update_user_profile_form = UpdateUserProfileForm(initial={'userPicture':profile.userPicture,'bio':profile.bio})

    return render(request, 'pethub/update-user.html', {'update_user_profile_form' : update_user_profile_form,
                                                       'update_user_form': update_user_form,
                                                       'updated': updated})



@login_required
def like(request):
    p_id = None
    if request.method == 'GET':
        p_id = request.GET['posts_id']
        likes = 0
    if p_id:
        # Fetch post for AJAX
        post = Post.objects.get(id=int(p_id))
        if post:
            #Check if user has liked the post before
            if request.user in post.liked_users.all():
                #if yes, remove them
                post.liked_users.remove(request.user)
            else:
                #if not, add them in
                post.liked_users.add(request.user)
            #Set likes count to number of liked users
            likes = post.liked_users.count()
            post.likes = likes
            post.save()
    return HttpResponse(likes)

@login_required
def search(request):

    #Try and get data if get method used
    if request.method == "GET":
        # get term user searched for
        search_term = request.GET.get("search_term", None)
            

    #filter posts based on search term
    posts = Post.objects.filter(tags__name__in=search_term.split()).order_by('-upload_date').distinct()
    post_list = paginate(posts, request)
    post_list = set_likes(post_list)
    return render(request, 'pethub/search.html', {'post_list' : post_list,
                                                  'search_term' : search_term,
                                                  'feed_required':True})

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user == request.user:
        Post.objects.get(id=post_id).delete()
    return user_profile(request, request.user.username)

@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        Comment.objects.get(id=comment_id).delete()
    return redirect(reverse('index'))

@login_required
def confirm_user_deletion(request,user_id):
    user = User.objects.get(id=user_id)
    
    if request.user == user:
        if request.method == "GET":
            return render(request, 'pethub/confirm-user-deletion.html', {'user' : user})
        elif request.method == "POST":
            
            if request.POST.get('submit') == "confirm_deletion":
                #get related userprofile
                up = user.userprofile
                
                #delete user profile
                up.delete()
                user.delete()
                return redirect(reverse('login'))
            elif request.POST.get('submit') == "refuse_deletion":
                
                return user_profile(request,user.username)
                
    else:
        return index(request)
    

@login_required
def add_comment(request,post_id):
    # boolean to show success of upload
    uploaded = False
    
    post = Post.objects.get(id=post_id)

    #Try and get data if POST method used
    if request.method == "POST":
        # fill in data from UserForm and UserProfileForm
            comment_form = CommentForm(data=request.POST)


            if comment_form.is_valid():
                # save user info to the database
                comment = comment_form.save(commit=False)

                # save associated user
                comment.user = request.user

                #Assign relevant post to comment
                comment.post = post
                
                

                # Save comment information
                comment.save()


                # show comment upload  was successful
                uploaded = True
                
            else:
                # form was invalid, print error message
                print(comment_form.errors,comment_form.errors)

    else:
        comment_form = CommentForm()


    context_dict = {'comment_form': comment_form,
                       'uploaded': uploaded,
                    'post' : post,}
    #Render template according to data received
    return render(request, 'pethub/add-comment.html', context_dict)
