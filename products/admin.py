from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'barCode', 'price', )
    list_display_links = ('id', 'name', 'barCode', )


admin.site.register(models.Product, ProductAdmin)