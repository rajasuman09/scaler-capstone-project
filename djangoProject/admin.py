from django.contrib import admin
from djangoProject.models import User, Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['title', 'username', 'name', 'email']
    list_display = [ 'username', 'name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    save_as = True
    fieldsets = (
        ("Product Info", {
            'fields': ('seller', 'name', 'description')
        }),
        ("Stock Info", {
            'fields': ('price', 'stock'),
            'classes': ('collapse',)
        })
    )