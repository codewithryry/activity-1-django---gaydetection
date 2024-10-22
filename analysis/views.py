from django.shortcuts import render

def home(request):
    return render(request, 'analysis/home.html')

def history(request):
    return render(request, 'analysis/history.html')

def summary(request):
    return render(request, 'analysis/summary.html')
