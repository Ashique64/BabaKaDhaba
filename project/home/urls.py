from django.urls import path
from .views import home, contact, menu, general_breakfast

urlpatterns = [
    path("", home, name="home"),
    path("menu/", menu, name="menu"),
    path("menu/general-breakfast", general_breakfast, name="general-breakfast"),
    path("contact/", contact, name="contact"),
]
