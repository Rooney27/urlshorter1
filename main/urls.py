from django.urls import path
from . import views
urlpatterns = [
    path("", views.urlShort, name="home"),
    path("myUrls", views.urlsHistory, name = "history"),
    path("<str:slugs>", views.urlRedirect, name="redirect"),
    
]