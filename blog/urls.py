from django.urls import path, re_path, include

from . import views

from mysite1.odin import views

from  django.views.generic import TemplateView


"""
urlpatterns = [
    
    '''
    # ex: /user/5/
    path('user/<int:user_id>', views.user, name='user'),
    # ex: /topic/5/
    path('topic/<int:topic_id>', views.topic, name='topic'),
    # ex: /message/5/
    path('message/<int:message_id>', views.message, name='message'),
    '''

    
]
"""

"""
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),

    path('mir', views.mir, kwargs={"first":"Даниэль", "second":"Давид"}),

    path('mir2', views.mir2),

    path('mir3', views.mir3),

#    re_path(r'^stih', views.stih),

    path('stishok', views.stishok),

    path('about1', views.about1, kwargs={"name":"Tom", "age": 38}),


#Гл.2, часть 5
  

    path('', views.index),
    path("oppar/<str:name>", views.oppar),
    path("oppar1/<name>/<int:age>", views.oppar1),


    path("oppar3", views.oppar3),
    path("oppar3/<name>", views.oppar3),
    path("oppar3/<name>/<int:age>", views.oppar3),

    re_path(r"^oppar4/(?P<name>\D+)/(?P<age>\d+)", views.oppar4),

    re_path(r"^oppar4_1/(?P<name>\D+)/(?P<age>\d+)", views.oppar4_1),
    re_path(r"^oppar4_1/(?P<name>\D+)", views.oppar4_1),
    re_path(r"^oppar4_1", views.oppar4_1),

]
"""
"""

#Гл.2, часть 6_1

product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
]
 
urlpatterns = [
    path("", views.index),
    path("products/", include(product_patterns)),
]



#Гл.2, часть 6_2

product_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]
 
urlpatterns = [
    path("", views.index),
    path("products/<int:id>/", include(product_patterns)),
]


#Гл.2, часть 7

urlpatterns = [
    path("", views.index),
    path("user/", views.user)
]

"""
#Гл.2, часть 8
# переадресация 

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details),


#  отправка статусных кодов


    path("index1/<int:id>", views.index1),
    path("access/<int:age>", views.access),

#Гл.2, часть 9
#отправка json

    path("index2/", views.index2),

    path("index3/", views.index3),

#Гл.2, часть 10
# установка куки

    path("set", views.set),

# получение куки    
    path("get", views.get),       

]

#Гл.3, часть 1 Шаблоны

urlpatterns = [
    path("first/", views.first),

    path("second/", views.second),

    path("third/", views.third),

#Гл.3, часть 2 
# Передача данных в Шаблоны

    path("first1/", views.first1),

# Передача сложных данных в Шаблоны

    path("fourth/", views.fourth),

#передача объектов классов

    path("fifth/", views.fifth),


#Гл.3, часть 3
#встроенные теги шаблонов
    path("date/", views.date),

#Гл.3, часть 4
#фильтры шаблонов
    path("filtr_shab/", views.filtr_shab),

#проверка значения
    path("valid/", views.valid),

#Гл.3, часть 5
#статические файлы
    
    path("stat_file/", views.stat_file),
    path("cat/", views.cat),

#Гл.3, часть 6
#TemplateView

    path("hello/", TemplateView.as_view(template_name="hello.html")),

    path("task/", TemplateView.as_view(template_name="task.html", 
        extra_context={"task": "Выполнить всё по инструкции!"})),

#Гл.3, часть 7
#Конфигурация шаблонов

    path("first2/", views.first2),

    path("first3/", views.first3),

#Гл.3, часть 8
#расширение шаблонов и фильтр extend

    path("glav/", views.glav),
    path("contacts/", views.contacts),
    path("stih/", views.stih),

]

