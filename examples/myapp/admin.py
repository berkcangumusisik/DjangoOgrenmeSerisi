from django.contrib import admin
from .models import Product, Category, Address, Supplier




class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'isActive', 'slug' , "selected_categories"]
    list_display_links = ['product_name', "price"]
    prepopulated_fields = {'slug': ('product_name',)}
    list_filter = ['product_name', 'price', "categories"]
    list_editable =["isActive"]
    search_fields = ['product_name', 'price']
    def selected_categories(self, obj):
        html =""
        for category in obj.categories.all():
            html += category.name + " "
        return html


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Supplier)