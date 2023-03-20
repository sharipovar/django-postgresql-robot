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
    return (read_file)



def index(request):
    return HttpResponse("<h2>Главная</h2>")
  
def about1(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)    

#Гл.2, часть 5

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

#Гл.2, часть 6_1

def products(request):
    return HttpResponse("Список товаров")
 
def new(request):
    return HttpResponse("Новые товары")
 
def top(request):
    return HttpResponse("Наиболее популярные товары")


#Гл.2, часть 6_2

def products(request, id):
    return HttpResponse(f"Товар {id}")
 
def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")
 
def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")

#Гл.2, часть 7
# значения по умолчанию определены

def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Не известно")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")



