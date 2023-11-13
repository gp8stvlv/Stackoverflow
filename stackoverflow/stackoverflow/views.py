from django.shortcuts import render

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def questionList(request):
    return render(request, 'questionList.html')

def settings(request):
    return render(request, 'settings.html')

def tag(request):
    return render(request, 'tag.html')

def question123(request):
    return render(request, 'question123.html')

def hot(request):
    return render(request, 'hot.html')


