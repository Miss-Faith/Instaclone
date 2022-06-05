from django.urls import path
from . import views
from django.contrib.auth import views as authViews 

urlpatterns = [
  path('signup/', views.Signup, name='signup'),
  path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
]