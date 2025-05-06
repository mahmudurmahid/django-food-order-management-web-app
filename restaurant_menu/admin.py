from django.contrib import admin
from .models import FoodItem

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "food_availability", "meal_type", "price", "author")
    list_filter = ("food_availability",)
    search_fields = ("meal", "description")

admin.site.register(FoodItem, MenuItemAdmin)