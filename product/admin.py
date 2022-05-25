from django.contrib import admin

from product import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'status', 'user', 'priority']
    autocomplete_fields = ['user']
    list_filter = ('name', 'status', 'user')
    list_editable = ('name',)
    list_display = (
        'id',
        'name',
        'status',
        'user',
        'priority',
        'created_at',
        'updated_at',
    )
    empty_value_display = '-empty-'


@admin.register(models.ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    search_fields = ('name', 'user')
    autocomplete_fields = ('user',)
    list_filter = ('name', 'user')
    list_editable = ('name',)
    list_display = (
        'id',
        'name',
        'user',
        'created_at',
        'updated_at',
    )
    empty_value_display = '-empty-'
