import uuid

from django.contrib.auth.models import AbstractUser
from django.core import exceptions

from django.core.exceptions import ValidationError
from django.db.models import Model, IntegerField, CharField, ForeignKey, PositiveIntegerField, BigAutoField, UUIDField, \
    SlugField, CASCADE
from django.utils import timezone
from django.utils.text import slugify


class User(AbstractUser):

    def clean(self):
        if self.username.lower() == "botir":
            raise ValidationError(" botir degan username qo'yib bo'lmaydi ")


# #
# # class Product(Model):
# #     name = models.CharField(max_length=255)
# #     price = models.DecimalField(max_digits=10, decimal_places=2)
# #     inventory = models.BigIntegerField()
# #     is_available = BooleanField(default=True)
# #     created_at = DateField(auto_now=False)
# #     available = DecimalField(max_digits=5,decimal_places=2)
# #     # book_created_at = DurationField()
# #     emails = EmailField()
# #     files = FileField(blank=True, null=True)
# #     # generate = GenericIPAddressField()
# #     jsons = JSONField(blank=True , null=True)
# #
# #
# #     def __str__(self):
# #         return self.name
# #
#
#
# # class Product(Model):
# #     name = models.CharField(max_length=255)
# #
# #     SCHEMA = {
# #         'type': 'dict',
# #         'keys': {
# #             'size': {
# #                 'type': 'number',
# #                 'default': 12,
# #             },
# #             'color': {
# #                 'type': 'string',
# #             },
# #
# #         },
# #     }
# #
# #     data = JSONField(schema=SCHEMA)
# #     slug = models.SlugField(unique=True, blank=True,editable=False)
# #
# #     def get_absolute_url(self):
# #         return reverse('product_detail', kwargs={'slug': self.slug})
# #     url = models.URLField(null=True, blank=True)
# #
# #     def clean(self):
# #         super().clean()
# #         if self.url:
# #             try:
# #                 response = requests.head(self.url, timeout=5)
# #                 if response.status_code >= 400:
# #                     raise ValidationError(f"The URL '{self.url}' is not reachable.")
# #             except requests.RequestException:
# #                 raise ValidationError(f"The URL '{self.url}' is not reachable.")
# #
# #     # def save(self, *args, init_id=None, **kwargs):
# #     #    if not init_id:
# #     #        self.save(*args,init_id=True)
# #     #
# #     #     super().save(*args, **kwargs)
#
#
#
# import uuid
# from django.db import models
#
# import uuid
# from django.db import models
# from django.utils.text import slugify
#
#
# class Category(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     slug = models.SlugField(unique=True, blank=True, editable=False)
#     name = models.CharField(max_length=100, unique=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#             while Category.objects.filter(slug=self.slug).exists():
#                 self.slug = f"{slugify(self.name)}-{uuid.uuid4().hex[:8]}"
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
#
#
# import uuid
# from django.db import models
# from django.utils.text import slugify
#
# class Product(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
#     slug = models.SlugField(unique=True, blank=True, editable=False)
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True, null=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#             while Product.objects.filter(slug=self.slug).exists():
#                 self.slug = f"{slugify(self.name)}-{uuid.uuid4().hex[:8]}"
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
#
#
# from django.db import models
#
# class ExampleModel(models.Model):
#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now=True)
#
#
#
# def __str__(self):
#         return self.name
#
#
#
# from django.db import models
# from calendar import month_name
#
#
#
#
# #
# # class Month(models.Model):
# #     class MonthChoice(models.IntegerChoices):
# #         choices = [(i, month_name[i]) for i in range(1, 13)]
# #
# #     month = models.IntegerField(choices=MonthChoice.choices)
#
#
# from django.db import models
# from django.core.exceptions import ValidationError
# from datetime import datetime
#
# def minute_validation(value):
#     current_minute = datetime.now().minute
#     if current_minute % 2 == 0:
#         raise ValidationError(
#             "bu vaqtda qo'sha olmaysiz ",
#             code='minute_error',
#             params={'value': current_minute}
#         )
#
# class MyModel(models.Model):
#     name = models.CharField(
#         max_length=100,
#         validators=[minute_validation],
#         error_messages={
#             'minute_error': "Minute %(value)s is not allowed; please try again later."
#         }
#     )
#     description = models.TextField()
#
#
#
#

#
# class Product(Model):
#     def query

def error_handler(value):
    minute = timezone.now().minute
    if minute % 2 != 0:
        raise exceptions.ValidationError('xabar', code='sai', params={'value': value})
    return value

class Category(Model):
    name = CharField(max_length=255)
    id = BigAutoField(primary_key=True)
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)  # unique=True qo'shildi
    slug = SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, init_id=None, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(Model):
    user = ForeignKey(User , CASCADE)
    name = CharField(max_length=255, validators=[error_handler], error_messages={"ixlos": '%(value)s vatq juft emas6'})
    category = ForeignKey('apps.Category', CASCADE, to_field='uuid')
    price = PositiveIntegerField(default=0)
    description = CharField(null=True)

