from django.shortcuts import render
from django.views import generic
from .models import FoodItem

# Create your views here.
class MenuListView(generic.ListView):
    queryset = FoodItem.object.order_by("-date_created")
    template_name = "index.html"


class MenuItemDetail(generic.DetailView):
    model = FoodItem
    template_name = "menu_item_detail.html"


