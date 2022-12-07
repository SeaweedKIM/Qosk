from django.contrib import admin
from .models import Customer, List, Favor, CartItem

# Register your models here.

admin.site.register(Customer)

# class Inline(admin.StackedInline):
#     model = List
#     extra = 1


class MenuAdmin(admin.ModelAdmin):
    # inlines: [Inline]
    list_display = ['food_name', 'price', 'explain', 'category','image' ]
    list_display_links = ['food_name']
    list_filter = ['category']
    search_fields = ['food_name']

    def explain(self, post):
        return post.food_explain[:10]

admin.site.register(List, MenuAdmin)


# admin.site.register(Bill)

admin.site.register(Favor)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['food', 'quantity']

admin.site.register(CartItem, OrderAdmin)