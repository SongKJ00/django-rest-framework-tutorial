from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root
from snippets import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
  path('', include(router.urls))
]

