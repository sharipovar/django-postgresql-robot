from django.urls import path, re_path, include

from . import views

from mysite1.odin import views




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

"""

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




