from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import InventoryForm

@login_required
def inventory_list(request):
    items = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'items': items})

@login_required
def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'add_inventory.html', {'form': form})

@login_required
def delete_inventory(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)
    item.delete()
    return redirect('inventory_list')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

