from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home_tweet(request):
    print request
    num=12
    return render(request, 'home.html', {'Num': num})
