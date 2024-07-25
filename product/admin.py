from django.contrib import admin

from .models import Category, Product, Brand


admin.site.register([Category, Product, Brand])