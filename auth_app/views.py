from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, "signup.html")

def handle_login(request):
    return render(request, "login.html")

def handle_logout(request):
    return render(request, "logout.html")
