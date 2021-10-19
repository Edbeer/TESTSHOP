from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title', 'author', 'slug', 'category',
                    'price', 'in_stock', 'created_at', 'updated_at']
    list_filter = ['price', 'in_stock']
    list_editable = ['price', 'in_stock']
