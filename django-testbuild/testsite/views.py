from django.shortcuts import render
from django.http import HttpResponse
from .models import PasswordEntryForm

# Create your views here.
def create_password_entry(request):
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Password entry created successfully!")
    else:
        form = PasswordEntryForm()
    return render(request, 'create_password_entry.html', {'form': form})