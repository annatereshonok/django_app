from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command


class Command(BaseCommand):
    help = "Add test categories and products to the database with fixture"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'data/category_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded categories from fixture'))

        call_command('loaddata', 'data/product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded products from fixture'))
