from django.contrib import admin
from .models import Product, Category




class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'isActive', 'slug','category' ]
    list_display_links = ['product_name', "price"]
    prepopulated_fields = {'slug': ('product_name',)}
    readonly_fields = ['slug']
    list_filter = ['product_name', 'price','category']
    list_editable =["isActive"]
    search_fields = ['product_name', 'price']
    


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
