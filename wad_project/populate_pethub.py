import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad_project.settings')

import django
django.setup()
from pethub.models import UserProfile, User, Post, Comment
from random import randint, choice

def populate():
    
    
    # List of dicitonaries of example users
    users = [{'username': 'AlexaK',
              'first_name': 'Alexa',
              'last_name': 'Kanetrot',
              'bio': "Hi! I'm Alexa and I'm a mature student of the University of Bristol. I love my kids, sometimes nearly as much as cute dogs.",
              'password': 'alexaK78',
              'userPicture': 'user_images/alexa_user_image.png',},

             {'username': 'Baroness_Barrington',
              'first_name': 'Jessie',
              'last_name': 'Barrington',
              'bio': """Hey, welcome to my profile! I'm really into talking about my pets to anyone who will listen. That and my business, Relish. Definitely give us a
visit if you're ever in Perth!""",
              'password': 'Relish',
              'userPicture': 'user_images/jessie_user_image.png',},

             {'username': 'DSyntop',
              'first_name': 'David',
              'last_name': 'Syntop',
              'bio': "My name's David and if you stick around for any length of time, I'll end up telling you about my dog.",
              'password': 'Paws_Newman',
              'userPicture': 'user_images/david_user_image.png',}]

    for user in users:
        add_profile(user['username'],user['first_name'],user['last_name'],user['password'],user['userPicture'],user['bio'])

    alexa = User.objects.get(username="AlexaK")
    jessie = User.objects.get(username="Baroness_Barrington")
    david = User.objects.get(username="DSyntop")

    
    #Create lists of dictionaries holding example posts
    posts = [
    {'title': 'Cute dogs hanging around Kelvingrove!',
     'liked_users': [david,jessie],
     'description': "Saw some ultra-cute puppies walking around Kelvingrove today, so cute!!",
     'user': alexa,
     'tags': "dogs,cute,adorable,playing,fluff",
     'picture': 'post_images/kg_dogs.jpg',},
    
    {'title': 'Adorably cute kittens',
     'liked_users': [alexa,david],
     'description': "Went to the cat cafe today and the little kittens were insanely cute; would recommend to all cat-lovers.",
     'user': jessie,
     'tags': "cats, coffee,playtime,chilling",
     'picture': 'post_images/cat_cafe.jpg',},

     {'title': "Can't wait to tell the grandkids about Rufus!",
     'liked_users': [alexa,jessie],
     'description': "Just got a new pup, Rufus, and I think the twins will love him! Keeping him a secret until they next come round, will keep you all posted!",
     'user': david,
     'tags': "puppy, dogs,surprise,playtime",
     'picture': 'post_images/rufus.jpg',},

    {'title': 'Cute kittens in Relish!',
     'liked_users': [david,alexa],
     'description': "Had the cutest kittens come into Relish today, hope these cuddly customers come back soon!",
     'user': jessie,
     'tags': "cute, cats,adorable,work",
     'picture': 'post_images/relish_kittens.jpg',},

    {'title': 'Kids loving the new hamster!',
     'liked_users': [david,jessie],
     'description': "My kids adore Harry the Hamster and can't wait to get home from school everyday to see him!",
     'user': alexa,
     'tags': "hamster,hutch",
     'picture': 'post_images/alexa_harry_hamster.jpg',},

    {'title': 'Harry has pretty much become part of the family',
     'liked_users': [david,jessie],
     'description': "Harry and the kids are getting along better than ever, look at what they got him to do!",
     'user': alexa,
     'tags': "hamster,cuddly,adorable,playing,fluff",
     'picture': 'post_images/alexa_harry_bed.jpg',},

    {'title': 'The adventures of paws newman',
     'liked_users': [alexa,jessie],
     'description': "The adventures of paws continues!",
     'user': david,
     'tags': "dogs,cute,adorable,handsome,boi",
     'picture': 'post_images/paws_newman.jpg',},]
    

    for post in posts:
        add_post(post['title'],post['liked_users'],post['description'],post['picture'],post['tags'],post['user'])

    comments = ["So cute!","Awww!","I love it!","Adorable!","Can't wait to hear more about this!","Tell me more!","This. This is why this site exists."]
    users = [david,jessie,alexa]
    
    for post in Post.objects.all():
        #select random comment from list
        comment_num = randint(0,len(comments)-1)
        #add comment to post
        add_comment(post,comments[comment_num], choice(users))
        #remove comment to reduce repetition
        comments.remove(comments[comment_num])
    
def add_post(title, liked_users, description, picture, tags, user):
    p = Post.objects.get_or_create(title=title)[0]
    for l_user in liked_users:
        p.liked_users.add(l_user)
    p.description = description
    for tag in tags.split(","):
        p.tags.add(tag)
    p.picture = picture
    p.user = user
    p.save()
    return p

def add_comment(post,comment_text,user):
    #save comment details
    comment = Comment.objects.get_or_create(comment_text=comment_text)[0]
    comment.post = post
    comment.comment_text = comment_text
    comment.user = user
    comment.save()
    return comment

def add_profile(username, first_name, last_name, password, userPicture, bio):
    
    u = User.objects.get_or_create(username=username)[0]
    u.first_name = first_name
    u.last_name = last_name
    u.set_password(password)
    u.save()
    
    up = UserProfile.objects.get_or_create(user=u)[0]
    up.userPicture = userPicture
    up.bio = bio
    up.save()
    return up

if __name__ == '__main__':
    print('Starting Pethub population script...')
    populate()

    
        
        
