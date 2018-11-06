from django.contrib import admin
from .models import Category,Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'purchase','wholesale','block_price','retail',
	'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['purchase','wholesale','block_price', 'available']
	prepopulated_fields = {'slug': ('name',)}