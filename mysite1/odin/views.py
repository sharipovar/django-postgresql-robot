"""from django.shortcuts import render

# Create your views here.
"""

from django.http import HttpResponse







def index(request):
    return HttpResponse("Главная")
 
def about(request):
    return HttpResponse("О сайте")

  
 
def contact(request):
    return HttpResponse("Контакты")

def mir(request,first,second):
    return HttpResponse(f"""
            <h2>Внуки:</h2>
            <p>первый: {first}</p>
            <p>второй: {second}</p>
    """)



def mir2(request):
    return HttpResponse("Здравствуй, МИР!!!")

def mir3(request):
    output="Привет, МИР!!! "
    output+="Здравствуй, МИР!!!  "
    output+="МИРУ МИР!!!"
    return HttpResponse(output)



def stishok(request):
    
    with open('stishok.txt', 'r') as file:
        read_file = file.read()
    return HttpResponse(read_file)



def index(request):
    return HttpResponse("<h2>Главная</h2>")
  
def about1(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)    

def oppar(request, name):
    return HttpResponse(f"<h2>Имя: {name}</h2>")
    
def oppar1(request, name, age):
    return HttpResponse(f"<h2>Имя: {name}  Возраст:{age}</h2>")

def oppar3(request, name="Undefined", age =0):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

def oppar4(request, name, age):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

def oppar4_1(request, name="Undefined", age =0):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

def products(request):
    return HttpResponse("Список товаров")
 
def new(request):
    return HttpResponse("Новые товары")
 
def top(request):
    return HttpResponse("Наиболее популярные товары")

