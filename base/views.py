from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')
def classroom(request):
    return render(request, 'classroom.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')