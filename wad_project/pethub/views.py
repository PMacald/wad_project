from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.


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

def login(request):
    # Get response early so we can gather cookie info
    response = render(request, 'pethub/login.html')
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
