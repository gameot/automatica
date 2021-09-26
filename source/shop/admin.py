from django.contrib import admin

from .models import Shop, Visit


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'worker')


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'lat', 'long', 'date')
    readonly_fields = ('shop', 'lat', 'long', 'date')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
