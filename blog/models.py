from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=90, blank=True)
    last_name = models.CharField(max_length=90, blank=True)
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Categories(models.Model):
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and Unique"),
        max_length=255,
        unique=True,
    )
    description = models.TextField()
    slug = models.SlugField(
        verbose_name=_("Category Safe URL"), max_length=255, unique=True
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Topics(models.Model):
    name = models.CharField(
        verbose_name=_("Topic name"), help_text=_("Required"), max_length=255
    )
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    description = models.TextField()

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        verbose_name=_("Title"), help_text=_("Required"), max_length=255
    )
    subtitle = models.TextField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    body = models.TextField()
    source = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title
