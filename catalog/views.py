from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm


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


class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_success_url(self):
        return reverse_lazy('catalog:catalog_detail', kwargs={'pk': self.object.pk})


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:catalog_list')


class CatalogDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = "catalog/catalog_confirm_delete.html"
    success_url = reverse_lazy('catalog:catalog_list')
