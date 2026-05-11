from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

def get_absolute_url(self):
    return reverse('category', kwargs={'cat_slug': self.slug})


class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Категория'
    )

    slug = models.SlugField(
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
    

class Women(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    photo = models.ImageField(
    upload_to='photos/%Y/%m/%d/',
    blank=True,
    null=True,
    default=None
)

    tags = models.ManyToManyField(
    TagPost,
    blank=True,
    related_name='tags'
)

    cat = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
    )

    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.SET_NULL,
    related_name='posts',
    null=True,
    default=None
)


    objects = models.Manager()          # стандартный менеджер
    published = PublishedModel()        # наш новый

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

class ServiceInfo(models.Model):
    post = models.OneToOneField(
        Women,
        on_delete=models.CASCADE,
        related_name='service_info'
    )

    duration = models.CharField(
        max_length=100,
        verbose_name='Время выполнения',
        blank=True
    )

    guarantee = models.CharField(
        max_length=100,
        verbose_name='Гарантия',
        blank=True
    )

    area = models.CharField(
        max_length=100,
        verbose_name='Площадь',
        blank=True
    )

    def __str__(self):
        return f'Информация для {self.post.title}'
