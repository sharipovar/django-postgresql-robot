"""from django.shortcuts import render

# Create your views here.
"""

from django.http import HttpResponse






"""

def index(request):
    return HttpResponse("Главная")
 
def about(request):
    return HttpResponse("О сайте")

  
 
def contact(request):
    return HttpResponse("Контакты")

"""    

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

#Гл.2, часть 8
# переадресация 
from django.http import  HttpResponseRedirect, HttpResponsePermanentRedirect 

"""
def index(request):
    return HttpResponse("Index")

"""    
 
def about(request):
    return HttpResponse("About")
 
def contact(request):
    return HttpResponseRedirect("/about")
 
def details(request):
    return HttpResponsePermanentRedirect("/")

#  отправка статусных кодов
def index1(request, id):
    people = ["Tom", "Bob", "Sam"]
    # если пользователь найден, возвращаем его
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    else:
        return HttpResponseNotFound("Not Found")
 
def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if(age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")

#Гл.2, часть 9
from django.http import JsonResponse
 
def index2(request):
    return JsonResponse({"name": "Tom", "age": 38})

#определение класса-сериализатора
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
 
def index3(request):
    bob = Person("Bob", 41)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)
 
class Person:
  
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека
 
class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)
    
#Гл.2, часть 10
# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response   

# получение куки
def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")

#Гл.3, часть 1 Шаблоны
from django.shortcuts import render

def first(request):
    return render(request, "first.htm")

def second(request):
    return render(request, "second.htm")

def third(request):
    return render(request, "third.htm")

#Гл.3, часть 2 
# Передача данных в Шаблоны
def first1(request):
    data = {"header": "Привет!", "message": "Добро пожаловать!"}
    return render(request, "first1.html", context=data)

# Передача сложных данных в Шаблоны
def fourth(request):
    header = "Данные пользователя"              # обычная переменная
    langs = ["Python", "Java", "C#"]            # список
    user ={"name" : "Tom", "age" : 23}          # словарь
    address = ("Абрикосовая", 23, 45)           # кортеж
  
    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "fourth.html", context=data)

#передача объектов классов
def fifth(request):
    return render(request, "fifth.html", context = {"person": Person("Tom")})
 
class Person:
  
    def __init__(self, name):
        self.name = name    # имя человека

#Гл.3, часть 3
#встроенные теги шаблонов
def date(request):
    return render(request, "date.html") 
    
#Гл.3, часть 4
#фильтр шаблонов
def filtr_shab(request):
    return render(request, "filtr_shab.html")     

#проверка значения
def valid(request):
    return render(request, "valid.html") 

#Гл.3, часть 5
#статические файлы
def stat_file(request):
    return render(request, "stat_file.html") 

def cat(request):
    return render(request, "cat.html")    

#Гл.3, часть 7
#Конфигурация шаблонов

#в mysite1
def first2(request):
    return render(request, "first2.html")  

#в odin
def first3(request):
    return render(request, "first3.html")  

#Гл.3, часть 8
#расширение шаблонов и фильтр extend
def glav(request):
    return render(request, "glav.html")
 
def contacts(request):
    return render(request, "contacts.html")

def stih(request):
    return render(request, "stih.html")

#Гл.3, часть 9
#вложенные шаблоны и фильтр include
def glav1(request):
    return render(request, "glav1.html")
def glav2(request):
    return render(request, "glav2.html")
def glav3(request):
    return render(request, "glav3.html")
#передача данных
def glav4(request):
    return render(request, "glav4.html")


 