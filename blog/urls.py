from django.urls import path, re_path

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


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),

    path('mir', views.mir, kwargs={"first":"Даниэль", "second":"Давид"}),

    path('mir2', views.mir2),

    path('mir3', views.mir3),

#    re_path(r'^stih', views.stih),

    path('stih', views.stih),


]
"""

  
urlpatterns = [
    path('', views.index),
    path('about', views.about, kwargs={"name":"Tom", "age": 38}),
]
"""