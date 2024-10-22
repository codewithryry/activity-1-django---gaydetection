from django.shortcuts import render

def index(request):
    return render(request, 'detection/index.html')

def profile(request):
    return render(request, 'detection/profile.html')

def results(request):
    return render(request, 'detection/results.html')

