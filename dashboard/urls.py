from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("predire/", views.predire, name="predire"),
    path("installation/", views.installation, name="installation"),
]
