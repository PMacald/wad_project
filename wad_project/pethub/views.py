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
