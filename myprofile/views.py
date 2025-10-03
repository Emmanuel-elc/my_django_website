from django.shortcuts import render

def home(request):
    return render(request, 'myprofile/home.html')

def about(request):
    return render(request, 'myprofile/about.html')

def projects(request):
    return render(request, 'myprofile/projects.html')

def contact(request):
    return render(request, 'myprofile/contact.html')
from django.shortcuts import render

def home(request):
    return render(request, 'myprofile/home.html')

def contacts(request):
    return render(request, 'myprofile/contacts.html')
