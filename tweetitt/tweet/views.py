from __future__ import unicode_literals

from django.shortcuts import render
from .models import Tweet

# Create your views here.

def home_tweet(request):
    print request
    num=12
    return render(request, 'home.html', {'Num': num})

#CRUD Create Retrive or Read Update Delete

# Retrive GET desde la base de datos
def tweet_detail_view(request):
    msg = "vista de detalle"
    return render(request, "tweets/detail_view.html", {'msg':msg})

def tweet_list_view(request):
    msg = "lista de tweets"
    return render(request, "tweets/list_view.html", {'msg':msg})
