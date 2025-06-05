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


def north_indianbreakfast(request):
    return render(request, 'north_indianbreakfast.html')

def south_indian_breakfast(request):
    return render(request, 'south_indianbreakfast.html')


def starter(request):
    return render(request,'starter.html')

def soup(request):
    return render(request,"soup.html")

def salad(request):
    return render(request,"salad.html")

def nsgravy(request):
    return render(request,"ns gravy.html")

def randb(request):
    return render(request,"randb.html")

def tandoori(request):
    return render(request,"tandoori.html")

def bread(request):
    return render(request,"bread.html")

def noodles(request):
    return render(request,"noodles.html")

def momo(request):
    return render(request,"momo.html")

def pizza(request):
    return render(request,"pizza.html")

def pasta(request):
    return render(request,"pasta.html")

def sizzler(request):
    return render(request,"sizzler.html")

def lasagna(request):
    return render(request,"lasagane.html")

def bakerysweets(request):
    return render(request,"bakery and sweets.html")

def aeratedbeverage(request):
    return render(request,"aerated beverage.html")

def burger(request):
    return render(request,"burger.html")

def coffee(request):
    return render(request,"coffee.html")

def coldcoffee(request):
    return render(request,"cold coffee.html")

def freshjuice(request):
    return render(request,"fresh juice.html")

def fruitssalad(request):
    return render(request,"fruitsalad.html")

def fruitswine(request):
    return render(request,"fruitwine.html")

def healthyjuice(request):
    return render(request,"healthyjuice.html")

def healthysalad(request):
    return render(request,"healthysalad.html")

def hotdrink(request):
    return render(request,"hot drink.html")

def icetea(request):
    return render(request,"ice tea.html")

def laasi(request):
    return render(request,"lassi.html")

def mocktail(request):
    return render(request,"mocktail.html")

def pancakes(request):
    return render(request,"pancakes.html")

def raita(request):
    return render(request,"raita.html")

def sandw(request):
    return render(request,"sandwitchandwrap.html")

def smoothie(request):
    return render(request,"smoothie.html")

def specaildesert(request):
    return render(request,"specialdesert.html")

def shake(request):
    return render(request,"shakes.html")


def bands(request):
    return render(request,"bands.html")
