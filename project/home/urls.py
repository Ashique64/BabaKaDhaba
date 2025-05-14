from django.urls import path
from .views import home, about, contact, menu

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("menu/", menu, name="menu"),
    path("contact/", contact, name="contact"),
]
