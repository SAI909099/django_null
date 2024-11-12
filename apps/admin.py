from django.contrib import admin

from .models import Product, MyModel

from django.contrib import admin
from .models import ExampleModel

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'inventory','is_available','created_at', 'available','emails','files','jsons')
#     list_filter = ('is_available',)
#     search_fields = ('name',)
#
#     def get_search_results(self, request, queryset, search_term):
#         queryset, use_distinct = super().get_search_results(request, queryset, search_term)
#
#         if search_term:
#             queryset |= self.model.objects.filter(jsons__icontains=search_term)
#
#         return queryset, use_distinct

#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'data','url','slug')
#     search_fields = ('name', 'slug', 'data__size', 'data__color')

from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('uuid',)
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('uuid', 'name', 'category', 'price', 'stock')
#     search_fields = ('name', 'category__name')
#     list_filter = ('category',)
#     ordering = ('name',)
#     readonly_fields = ('uuid',)
#
#
# from django.utils import timezone
#
# @admin.register(ExampleModel)
# class ExampleModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'created_at_local', 'updated_at_local')
#
#     def created_at_local(self, obj):
#         return timezone.localtime(obj.created_at)
#
#     def updated_at_local(self, obj):
#         return timezone.localtime(obj.updated_at)
#
#     created_at_local.short_description = 'Created At (Tashkent Time)'
#     updated_at_local.short_description = 'Updated At (Tashkent Time)'
@admin.register(MyModel)
class Mymodel(admin.ModelAdmin):
    pass