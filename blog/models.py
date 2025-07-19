from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog_previews/",
        verbose_name="Превью",
        blank=True,
        null=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )
    view_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров"
    )

    def __str__(self):
        return f"{self.title} — {self.date_created:%d.%m.%Y}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["-date_created"]
