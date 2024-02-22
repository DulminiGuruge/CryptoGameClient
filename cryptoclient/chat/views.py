from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chat/chatbox.html", {"chat_box_name": chat_box_name})


def course_chat_room(request):
    try:
        # retrieve course with given id joined by the current user
        return render(request, 'chat/room.html')
    except:
        # user is not a student of the course or course does not exist
        return HttpResponseForbidden()
    