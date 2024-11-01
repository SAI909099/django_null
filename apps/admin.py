from django.contrib import admin

from .models import Product


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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'data','url','slug')
    search_fields = ('name', 'slug', 'data__size', 'data__color')

