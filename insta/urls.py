from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
		path('accounts/profile/', UserProfile, name='profile'),
		path('accounts/profile/follow/', UserProfileFollow, name='profile_follow'),
		path('signup/',signup,name = 'signup'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name = 'logout'),
   	path('newpost/', NewPost, name='newpost'),
		path('search/', search_results, name='search_results'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
    path('follow/<username>/<int:option>', follow, name='follow'),
		# path('unfollow/<username>', unfollow, name='unfollow'),
   	path('<uuid:post_id>/like', like, name='postlike'),
   	path('tag/<slug:tag_slug>', tags, name='tags'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

