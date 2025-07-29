from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Создаёт группу 'Модератор продуктов' и добавляет в неё нужные права и пользователя"

    def handle(self, *args, **kwargs):
        group_name = 'Модератор продуктов'
        user_email = 'anvtereshonok@gmail.com'

        user, created = User.objects.get_or_create(email=user_email)
        if created:
            user.set_password("user123+")
            user.save()
            self.stdout.write(self.style.SUCCESS(f"👤 Пользователь {user_email} создан"))

        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            self.stdout.write(self.style.SUCCESS(f"✅ Группа создана: {group_name}"))
        else:
            self.stdout.write(self.style.WARNING(f"⚠️ Группа уже существует: {group_name}"))

        try:
            unpublish_permission = Permission.objects.get(codename='can_unpublish_product')
            delete_permission = Permission.objects.get(codename='delete_product')
        except Permission.DoesNotExist as e:
            self.stderr.write(self.style.ERROR(f"❌ Не найдено разрешение: {e}"))
            return

        group.permissions.set([unpublish_permission, delete_permission])
        self.stdout.write(self.style.SUCCESS(f"✅ Права добавлены в группу '{group_name}'"))

        try:
            user = User.objects.get(email=user_email)
            user.groups.add(group)
            self.stdout.write(self.style.SUCCESS(f"👤 Пользователь {user.email} добавлен в группу"))
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"❌ Пользователь с email {user_email} не найден"))

