from django.contrib import admin
from .models import Product




class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'isActive', 'slug' ]
    list_display_links = ['product_name', "price"]
    readonly_fields = ['slug']
    list_filter = ['product_name', 'price','category']
    list_editable =["isActive"]
    search_fields = ['product_name', 'price']
    


admin.site.register(Product, ProductAdmin)
