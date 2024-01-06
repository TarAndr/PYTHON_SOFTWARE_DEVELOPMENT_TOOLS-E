# views.py

from django.shortcuts import render, redirect
from .forms import HumanForm

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Перенаправление на страницу успеха или другую страницу
    else:
        form = HumanForm()

    return render(request, 'add_human.html', {'form': form})
