from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Item, ItemAdmin)
