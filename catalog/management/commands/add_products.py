from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = "Заполняет базу тестовыми категориями и продуктами для Skystore"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING("Все категории и продукты удалены."))

        # --- Категории для Skystore ---
        categories_data = [
            {
                "name": "VS Code Plugins",
                "description": "Расширения и утилиты для повышения продуктивности в VS Code.",
            },
            {
                "name": "Django Templates",
                "description": "Готовые шаблоны и компоненты для Django-проектов.",
            },
            {
                "name": "Code Snippets & Utils",
                "description": "Небольшие, но полезные куски кода для Python и JavaScript.",
            },
        ]

        categories = {}
        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            categories[category.name] = category
            self.stdout.write(self.style.SUCCESS(f"✅ Категория создана: {category.name}"))

        # --- Продукты ---
        products_data = [
            {
                "name": "Auto Import",
                "description": "Плагин для VS Code, автоматически добавляющий импорты в Python-коде.",
                "price": Decimal("3.99"),
                "category": categories["VS Code Plugins"],
            },
            {
                "name": "Tailwind Class Helper",
                "description": "Инструмент для быстрой генерации классов Tailwind в HTML.",
                "price": Decimal("2.49"),
                "category": categories["VS Code Plugins"],
            },
            {
                "name": "Django Admin Dark",
                "description": "Темная тема для админки Django, совместимая с Bootstrap 5.",
                "price": Decimal("4.99"),
                "category": categories["Django Templates"],
            },
            {
                "name": "Login+Email Template",
                "description": "Готовая аутентификация с подтверждением по почте и восстановлением пароля.",
                "price": Decimal("6.99"),
                "category": categories["Django Templates"],
            },
            {
                "name": "Stripe Snippet",
                "description": "Простой сниппет для подключения Stripe в Django-проекте.",
                "price": Decimal("1.99"),
                "category": categories["Code Snippets & Utils"],
            },
            {
                "name": "JWT Auth для DRF",
                "description": "Мини-библиотека авторизации через JWT для Django REST Framework.",
                "price": Decimal("3.50"),
                "category": categories["Code Snippets & Utils"],
            },
            {
                "name": "Meta Tags for SEO",
                "description": "Утилита для добавления SEO-мета-тегов в Django-шаблоны.",
                "price": Decimal("2.00"),
                "category": categories["Django Templates"],
            },
            {
                "name": "Prettier Config",
                "description": "Готовый конфиг Prettier + ESLint для фронтенд-проектов.",
                "price": Decimal("1.00"),
                "category": categories["Code Snippets & Utils"],
            },
            {
                "name": "Notebook Tools",
                "description": "Плагин для удобной работы с Jupyter в VS Code.",
                "price": Decimal("2.99"),
                "category": categories["VS Code Plugins"],
            },
            {
                "name": "Social Login Pack",
                "description": "Быстрая интеграция входа через Google, GitHub и VK.",
                "price": Decimal("5.49"),
                "category": categories["Django Templates"],
            },
        ]

        for prod_data in products_data:
            product = Product.objects.create(**prod_data)
            self.stdout.write(self.style.SUCCESS(f"🛒 Продукт создан: {product.name}"))

        self.stdout.write(self.style.SUCCESS("🎉 База успешно заполнена для Skystore!"))
