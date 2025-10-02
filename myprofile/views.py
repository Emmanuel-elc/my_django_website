from django.shortcuts import render

def home(request):
    return render(request, 'myprofile/home.html')  # include the app folder
