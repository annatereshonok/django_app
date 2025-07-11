from django.shortcuts import render, get_object_or_404
from .models import Product


def show_home(request):
    if request.method == "GET":
        products = Product.objects.all()
        rows = [products[i:i + 4] for i in range(0, len(products), 4)]
        context = {'rows': rows}
        return render(request, "catalog/home.html", context)


def show_contacts(request):
    if request.method == "GET":
        return render(request, "catalog/contacts.html")


def show_product(request, pk):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        context = {"product": product}
        return render(request, "catalog/product.html", context)
