from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("mining/", views.room, name="room"),
]

""" from django.urls import path
from . import views
app_name = 'chat'

urlpatterns = [
    
    path("<str:room_name>/", views.room, name="room"),
    #path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
    #path('room/', views.course_chat_room,name='course_chat_room'),
] """