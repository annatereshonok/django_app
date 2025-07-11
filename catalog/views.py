from django.views.generic import DetailView, ListView, TemplateView
from .models import Product


class CatalogListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "rows"

    def get_queryset(self):
        products = Product.objects.all()
        return [products[i:i + 4] for i in range(0, len(products), 4)]


class CatalogDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"


class CatalogTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"
