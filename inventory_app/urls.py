from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.add_inventory, name='add_inventory'),
    path('inventory/delete/<int:item_id>/', views.delete_inventory, name='delete_inventory'),
]
