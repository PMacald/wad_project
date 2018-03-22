import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad_project.settings')

import django
django.setup()
from pethub.models import UserProfile, User, Post

def populate():
    
    
    # List of dicitonaries of example users
    users = [{'username': 'AlexaK',
              'first_name': 'Alexa',
              'last_name': 'Kanetrot',
              'bio': "Hi! I'm Alexa and I'm a mature student of the University of Bristol. I love my kids, sometimes nearly as much as cute dogs.",
              'password': 'alexaK78',
              'userPicture': None,},

             {'username': 'Baroness_Barrington',
              'first_name': 'Jessie',
              'last_name': 'Barrington',
              'bio': """Hey, welcome to my profile! I'm really into talking about my pets to anyone who will listen. That and my business, Relish. Definitely give us a
visit if you're ever in Perth!""",
              'password': 'Relish',
              'userPicture': None,},

             {'username': 'DSyntop',
              'first_name': 'David',
              'last_name': 'Syntop',
              'bio': "My name's David and if you stick around for any length of time, I'll end up telling you about my dog.",
              'password': 'Paws_Newman',
              'userPicture': None,},]

    for user in users:
        add_profile(user['username'],user['first_name'],user['last_name'],user['password'],user['userPicture'],user['bio'])

    

    
    #Create lists of dictionaries holding example posts
    posts = [
    {'title': 'Cute dogs hanging around Kelvingrove!',
     'likes': 23,
     'description': "Saw some ultra-cute puppies walking around Kelvingrove today, so cute!!",
     'user': User.objects.get(username="AlexaK"),
     'tags': "dogs, cute, adorable, playing, fluff",
     'picture': None,},
    
    {'title': 'Adorably cute kittens',
     'likes': 40,
     'description': "Went to the cat cafe today and the little kittens were insanely cute; would recommend to all cat-lovers.",
     'user': User.objects.get(username="Baroness_Barrington"),
     'tags': "cats, coffee, playtime, chilling",
     'picture': None,},

     {'title': "Can't wait to tell the grandkids about Rufus!",
     'likes': 54,
     'description': "Just got a new pup, Rufus, and I think the twins will love him! Keeping him a secret until they next come round, will keep you all posted!",
     'user': User.objects.get(username="DSyntop"),
     'tags': "puppy, dogs, surprise, playtime",
     'picture': None,}]
    

    for post in posts:
        add_post(post['title'],post['likes'],post['description'],post['picture'],post['tags'],post['user'])

    for i in range(0,20):
        add_post(str(i),i,"test_post",None, ["help", "this", "isn't", "working"], User.objects.get(username="DSyntop"))
        print("hello")
    
def add_post(title, likes, description, picture, tags, user):
    p = Post.objects.get_or_create(title=title)[0]
    p.likes = likes
    p.description = description
    p.tags = tags
    p.picture = picture
    p.user = user
    p.save()
    return p

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

    
        
        
