from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from decimal import Decimal
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Заполняет базу тестовыми категориями и продуктами для Skystore"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING("Все категории и продукты удалены."))

        # Создаём владельца
        owner, created = User.objects.get_or_create(email="admin@skystore.local")
        if created:
            owner.set_password("admin123")
            owner.is_staff = True
            owner.is_superuser = True
            owner.save()
            self.stdout.write(self.style.SUCCESS("👤 Пользователь admin@skystore.local создан"))

        # --- Категории ---
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
        ]

        for prod_data in products_data:
            product = Product.objects.create(
                **prod_data,
                owner=owner,
                is_published=True
            )
            self.stdout.write(self.style.SUCCESS(f"🛒 Продукт создан: {product.name}"))

        self.stdout.write(self.style.SUCCESS("🎉 База успешно заполнена для Skystore!"))
