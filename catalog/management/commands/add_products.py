from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = "Add test categories and products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_data = [
            {"name": "Электроника", "description": "Гаджеты и устройства"},
            {"name": "Одежда", "description": "Мужская и женская одежда"},
            {"name": "Книги", "description": "Художественная и научная литература"},
        ]

        categories = {}
        for cat_data in categories_data:
            category, _ = Category.objects.get_or_create(**cat_data)
            categories[category.name] = category
            self.stdout.write(
                self.style.SUCCESS(
                    f"Категория: {category.name} добавлена или уже существует."
                )
            )

        products_data = [
            {
                "name": "Смартфон XPhone 12",
                "description": "Современный смартфон с OLED-дисплеем",
                "price": Decimal("699.99"),
                "category": categories["Электроника"],
            },
            {
                "name": "Наушники NoiseBeat",
                "description": "Беспроводные наушники с шумоподавлением",
                "price": Decimal("199.99"),
                "category": categories["Электроника"],
            },
            {
                "name": "Футболка Oversize",
                "description": "Чёрная оверсайз футболка, хлопок",
                "price": Decimal("24.99"),
                "category": categories["Одежда"],
            },
            {
                "name": "Куртка зимняя",
                "description": "Утеплённая парка с капюшоном",
                "price": Decimal("129.90"),
                "category": categories["Одежда"],
            },
            {
                "name": "Джинсы Straight Fit",
                "description": "Синие джинсы прямого кроя",
                "price": Decimal("59.50"),
                "category": categories["Одежда"],
            },
            {
                "name": "Рюкзак Urban",
                "description": "Городской рюкзак с отделением под ноутбук",
                "price": Decimal("49.99"),
                "category": categories["Одежда"],
            },
            {
                "name": "Преступление и наказание",
                "description": "Роман Ф.М. Достоевского",
                "price": Decimal("14.00"),
                "category": categories["Книги"],
            },
            {
                "name": "1984",
                "description": "Роман-антиутопия Дж. Оруэлла",
                "price": Decimal("12.00"),
                "category": categories["Книги"],
            },
            {
                "name": "Гарри Поттер и философский камень",
                "description": "Книга Дж. К. Роулинг",
                "price": Decimal("18.75"),
                "category": categories["Книги"],
            },
            {
                "name": "Мастер и Маргарита",
                "description": "Классика М. Булгакова",
                "price": Decimal("15.00"),
                "category": categories["Книги"],
            },
        ]

        for prod_data in products_data:
            product, created = Product.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"✔ Продукт добавлен: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"⚠ Уже существует: {product.name}")
                )
