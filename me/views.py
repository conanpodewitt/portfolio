from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'me/index.html', context)

def cv(request):
    context = {}
    return render(request, 'me/index.html', context)