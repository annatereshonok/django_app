from django.views.generic import ListView, DetailView, TemplateView, View
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from .services import ProductService

from .models import Product
from .forms import ProductForm


class CreatorOrPermRequiredMixin(PermissionRequiredMixin):
    raise_exception = True

    def has_permission(self):
        obj = self.get_object()
        return (
            self.request.user == getattr(obj, 'owner', None) or
            super().has_permission()
        )


class CatalogListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "rows"

    def get_queryset(self):
        products = Product.objects.filter(is_published=True).all()
        return [products[i:i + 4] for i in range(0, len(products), 4)]


@method_decorator(cache_page(60 * 15), name='dispatch')
class CatalogDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"


class CatalogTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_success_url(self):
        return reverse_lazy('catalog:catalog_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации.")

        product.is_published = False
        product.save()
        return redirect('catalog:catalog_detail', pk=pk)


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:catalog_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            return HttpResponseForbidden("У вас нет доступа к редактированию этого продукта.")
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CatalogDeleteView(LoginRequiredMixin, CreatorOrPermRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = "catalog/catalog_confirm_delete.html"
    success_url = reverse_lazy('catalog:catalog_list')
    permission_required = 'catalog.delete_product'


class CategoryListView(ListView):
    model = Product
    template_name = "catalog/products_by_category.html"
    context_object_name = "category_products"

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        key = f'category_products_{category_id}'

        queryset = cache.get(key)
        if not queryset:
            queryset = ProductService.get_products_by_category(category_id)
            cache.set(key, queryset, 60 * 15)

        return [queryset[i:i + 4] for i in range(0, len(queryset), 4)]

