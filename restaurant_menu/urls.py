from django.urls import path
from . import views

urlpatterns = [
    path("", views.MenuListView.as_view(), name="home"),
    path("", views.MenuItemDetail.as_view(), name="menu_item_detail"),
]
