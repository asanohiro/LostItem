# photos/views.py
from django.shortcuts import render, redirect
from .forms import LostItemForm
from .models import LostItem

def upload_lost_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('map_view')
    else:
        form = LostItemForm()
    return render(request, 'upload.html', {'form': form})


def map_view(request):
    items = LostItem.objects.all()
    return render(request, 'map.html', {'items': items})
