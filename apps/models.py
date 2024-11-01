import requests
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model, SlugField, URLField
from django_jsonform.models.fields import JSONField
from functools import partial
from django.utils.text import slugify
from django.urls import reverse

class User(AbstractUser):

    def clean(self):
        if self.username.lower() == "botir":
            raise ValidationError(" botir degan username qo'yib bo'lmaydi ")


#
# class Product(Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inventory = models.BigIntegerField()
#     is_available = BooleanField(default=True)
#     created_at = DateField(auto_now=False)
#     available = DecimalField(max_digits=5,decimal_places=2)
#     # book_created_at = DurationField()
#     emails = EmailField()
#     files = FileField(blank=True, null=True)
#     # generate = GenericIPAddressField()
#     jsons = JSONField(blank=True , null=True)
#
#
#     def __str__(self):
#         return self.name
#


class Product(Model):
    name = models.CharField(max_length=255)

    SCHEMA = {
        'type': 'dict',
        'keys': {
            'size': {
                'type': 'number',
                'default': 12,
            },
            'color': {
                'type': 'string',
            },

        },
    }

    data = JSONField(schema=SCHEMA)
    slug = models.SlugField(unique=True, blank=True,editable=False)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
    url = models.URLField(null=True, blank=True)

    def clean(self):
        super().clean()
        if self.url:
            try:
                response = requests.head(self.url, timeout=5)
                if response.status_code >= 400:
                    raise ValidationError(f"The URL '{self.url}' is not reachable.")
            except requests.RequestException:
                raise ValidationError(f"The URL '{self.url}' is not reachable.")

    def save(self, *args, **kwargs):
        if not self.slug:  # Only create a slug if it’s not already set
            base_slug = slugify(self.name)
            slug = f"{base_slug}-1"
            counter = 2

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

def __str__(self):
        return self.name
