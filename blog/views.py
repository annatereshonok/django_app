from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save(update_fields=["view_count"])

        if obj.view_count == 100:
            send_mail(
                subject=f"🥳 Ура! Статья набрала 100 просмотров!",
                message=f"Поздравляем! Ваша статья '{obj.title}' достигла 100 просмотров.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['anvtereshonok@gmail.com'],
                fail_silently=True,
            )

        return obj


class BlogDeleteView(DeleteView):
    model = Blog
    context_object_name = 'blog'
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy('blog:blog_list')


class BlogFormBase:
    model = Blog
    fields = ['title', 'content', 'preview', 'is_published']
    context_object_name = 'blog'
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogCreateView(BlogFormBase, CreateView):
    pass


class BlogUpdateView(BlogFormBase, UpdateView):
    pass
