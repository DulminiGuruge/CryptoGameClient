# accounts/urls.py
from django.urls import path

from .views import SignUpView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'



urlpatterns = [
   # path('', views.index, name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('signup/', views.user_signup, name='signup'),
    #path('logout/', views.user_logout, name='logout'),
]