from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def detail(request):
    return render(request, 'detail.html')


def new(request):
    return render(request, 'new.html')