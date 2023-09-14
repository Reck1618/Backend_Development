from django.http import JsonResponse
from django.shortcuts import render
from .forms import EntryForm

# Create your views here.

def formView(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'success'})
    else:
        form = EntryForm()
    return render(request, 'form.html', {'form': form})

