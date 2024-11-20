from django.contrib import admin

from apps.models import Product, Category


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    # list_display = ('name'
    # )
    search_fields = ('data__size', 'data__color',)

    # search_fields = ('name',)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'id')

