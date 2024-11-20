import os
import django
from django.db.models import Count, F, Sum, Q

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Product, User
from django.db.models import Sum
#
# results = Product.objects.values('name', 'category__id').annotate(total=Sum('price'),count=Count('name'))
#
# for result in results:
#     print(result)


from django.db.models import F
from django.db.models.functions import Lower
# from django.db import transaction
#
#
# vowels = ('a', 'e', 'i', 'o', 'u', 'y')
#
# latest_user = User.objects.latest('date_joined')
#
# products = Product.objects.filter(user=latest_user)
#
# with transaction.atomic():
#     for product in products:
#         if product.name[0].lower() in vowels:
#             product.price = F('price') + 1000
#             product.save()
#
#     print(f"Product Name: {product.name}, Price: {product.price}")
#

#
# user_info = User.objects.filter(date_join = 2020)

filters = Product.objects.filter(
    Q(price__gte=2000, price__lte=3500) & Q(description__isnull=False) & Q(name__icontains='a')
)
for product in filters:
    print(f"Name: {product.name}, Price: {product.price}, Description: {product.description}")