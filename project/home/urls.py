from django.urls import path
from .views import home, contact, menu

urlpatterns = [
    path("", home, name="home"),
    path("menu/", menu, name="menu"),
    path("contact/", contact, name="contact"),
]
