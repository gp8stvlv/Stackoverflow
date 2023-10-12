from django.shortcuts import render

def Getbase(request):
    return render(request, 'base.html')

def ask(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'index.html')

def question(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'index.html')
