from django.urls import path, include 
from .views import register, user_login, home, user_logout, index
 
urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
]