from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["place", "desc"]


admin.site.register(Product, ProductAdmin)

