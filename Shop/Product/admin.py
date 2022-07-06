from django.contrib import admin
from .models import Product, Producer, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Producer)
admin.site.register(Category)