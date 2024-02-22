from django.urls import path
from . import views
app_name = 'chat'

urlpatterns = [
   
    path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
    #path('room/', views.course_chat_room,name='course_chat_room'),
]