from django.urls import path
from .views import (
    CatalogDetailView,
    CatalogTemplateView,
    CatalogListView,
    CatalogCreateView,
    CatalogUpdateView,
    CatalogDeleteView
)

app_name = "catalog"

urlpatterns = [
    path("", CatalogListView.as_view(), name="catalog_list"),
    path("product/<int:pk>/", CatalogDetailView.as_view(), name="catalog_detail"),
    path("product/<int:pk>/edit/", CatalogUpdateView.as_view(), name="catalog_update"),
    path("product/create/", CatalogCreateView.as_view(), name="catalog_create"),
    path("product/<int:pk>/delete/", CatalogDeleteView.as_view(), name="catalog_delete"),
    path("contacts/", CatalogTemplateView.as_view(), name="catalog_contacts"),
]
