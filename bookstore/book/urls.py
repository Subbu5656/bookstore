from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
 
urlpatterns =[
    path('', home,name='home'),
    path('login/', loginPage,name='login'),
    path('addbook/', addbook,name='addbook'),
    path('addbook/<id>/', addbook_id, name='addbook_id'),
    path('updatebook/<id>/', updatebook, name='updatebook'),
    path('register/', registerPage,name='register'),
    path('logout/', logoutPage,name='logout'),
    path('deletebook/<id>/', deletebook, name='deletebook'),
]