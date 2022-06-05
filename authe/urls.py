from django.urls import path
from . import views
from django.contrib.auth import views as authViews 

urlpatterns = [
  path('signup/', views.Signup, name='signup'),
  path('', authViews.LoginView.as_view(template_name='index.html'), name='index'),
  path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
]