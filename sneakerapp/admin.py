from django.contrib import admin
from sneakerapp.models import Product

# Register your models here.
# admin.site.register(Product)

# Define model admin class
class ProductAdminClass(admin.ModelAdmin):
   list_display=['name','cat','price','status']
   list_filter=['status','cat']

admin.site.register(Product,ProductAdminClass)
admin.site.site_header='Sneakerhead'

