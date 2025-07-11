from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.show_home, name="home"),
    path("product/<int:pk>", views.show_product, name="product"),
    path("contacts/", views.show_contacts, name="contacts"),
]
