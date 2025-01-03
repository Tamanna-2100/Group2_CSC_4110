from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')

def project1(request):
    return render(request, 'Project1.html')

def project2(request):
    return render(request, 'Project2.html')

def project3(request):
    return render(request, 'Project3.html')