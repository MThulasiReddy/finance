from django.urls import path
from . import views

urlpatterns = [
    
    
    path('',views.home,name='home'),
    path('addloan/',views.addloan,name='addloan'),
    path('login/',views.user_login,name='user_login'),


]