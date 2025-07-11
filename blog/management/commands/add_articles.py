from django.core.management.base import BaseCommand
from django.utils import timezone
from random import randint, choice

from blog.models import Blog


class Command(BaseCommand):
    help = "Заполняет базу блогов"

    def handle(self, *args, **kwargs):
        Blog.objects.all().delete()
        self.stdout.write(self.style.WARNING("Все категории и продукты удалены."))

        titles = [
            "5 причин попробовать Django",
            "Как написать Telegram-бота за вечер",
            "Чеклист для запуска pet-проекта",
            "Где брать идеи для проектов?",
            "Тёмная тема: за и против",
            "Как я сделал блог за час",
            "Python против JavaScript: битва титанов",
            "Зачем нужен Docker начинающему",
            "Как устроиться на первую работу",
            "Ошибки джуна на старте (и как их избежать)"
        ]

        for i, title in enumerate(titles):
            blog = Blog.objects.create(
                title=title,
                content=f"Это пример содержимого для статьи под названием «{title}». Здесь мог бы быть ваш крутой текст 🙂",
                is_published=True,
                view_count=randint(0, 50),
                date_created=timezone.now()
            )
            self.stdout.write(self.style.SUCCESS(f"✔ Статья добавлена: {blog.title}"))
