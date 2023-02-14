from django.urls import path, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from .views import *

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'song_entries', SongEntryViewSet)
router.register(r'songs', SongViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v1',
      description="Music API docs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
]

urlpatterns += router.urls


