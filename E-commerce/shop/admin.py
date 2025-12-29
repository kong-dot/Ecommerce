from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','product_image','category','selling_price')

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)


