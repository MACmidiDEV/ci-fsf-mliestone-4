from django.shortcuts import render, request

# Create your views here.


def index(request):
    return render(request, 'home/index.html')
