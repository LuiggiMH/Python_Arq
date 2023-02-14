from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, "core/home.html")

def about (request):
    return render(request, "core/about.html")

def project (request):
    return render(request, "core/project.html")

def contact (request):
    return render(request, "core/contact.html")

def team (request):
    return render(request, "core/team.html")