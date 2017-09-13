from django.shortcuts import render


def home(request):
    print request
    num=12
    return render(request, 'home.html', {'Num': num})
# Create your views here.
