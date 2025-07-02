from django.shortcuts import render


def show_home(request):
    if request.method == "GET":
        return render(request, "catalog/home.html")


def show_contacts(request):
    if request.method == "GET":
        return render(request, "catalog/contacts.html")
