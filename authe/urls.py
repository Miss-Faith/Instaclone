from django.urls import path
from django.contrib.auth import views as authViews 
from .views import *

urlpatterns = [
    path('signup/', Signup, name='signup'),
   	path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
]