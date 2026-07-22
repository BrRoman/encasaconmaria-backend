from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_category', 'name',
                    'get_description', 'price', 'featured']

    def get_category(self, obj):
        return obj.category

    def get_description(self, obj):
        if len(obj.description) > 70:
            return f'''{obj.description[:70]}…'''
        return obj.description


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
