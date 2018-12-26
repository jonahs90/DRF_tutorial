from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),

]
