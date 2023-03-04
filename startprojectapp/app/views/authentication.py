from django.shortcuts import render

def login(request):
    return render(request, "app/authentication/login.html")

def index(request):
    return render(request, "app/index.html")

def sample_error_500(request):
    '''
    Method for test the 500 Error
    '''
    ope = 100/0

    return render(request, "app/index.html", {})