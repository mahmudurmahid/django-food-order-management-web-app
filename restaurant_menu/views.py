from django.shortcuts import render
from django.views import generic
from .models import FoodItem, MEAL_TYPE

# Create your views here.
class MenuList(generic.ListView):
    queryset = FoodItem.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = FoodItem
    template_name = "menu_item_detail.html"
