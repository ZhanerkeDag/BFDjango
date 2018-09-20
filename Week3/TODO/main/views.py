from django.shortcuts import render

def index(request):
    return render(request, 'main/homePage.html')

# Create your views here.
