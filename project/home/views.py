from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def general_breakfast(request):
    return render(request, 'general-breakfast.html')
