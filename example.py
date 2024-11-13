import os
import django
from django.db.models import Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Product, Person

# print(Product.objects.filter(name='book'))


# print(Product.objects.exclude(name='kitob'))
#
# for i in Product.objects.annotate(bir = Count('name')):
#     print (i.name)

# products = Product.objects.annotate(name_count=Count('name'))

# for product in products:
#     print(product.name, product.name_count)

# print(Product.objects.order_by('id'))

# print(Person.objects.order_by('-age'))

