from django.urls import path
from .views import CatalogDetailView, CatalogTemplateView, CatalogListView

app_name = "catalog"

urlpatterns = [
    path("", CatalogListView.as_view(), name="catalog_list"),
    path("product/<int:pk>/", CatalogDetailView.as_view(), name="catalog_detail"),
    path("contacts/", CatalogTemplateView.as_view(), name="catalog_contacts"),
]
