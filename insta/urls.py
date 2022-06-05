from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
   	path('newpost/', NewPost, name='newpost'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
   	path('<uuid:post_id>/like', like, name='postlike'),
   	path('tag/<slug:tag_slug>', tags, name='tags'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
