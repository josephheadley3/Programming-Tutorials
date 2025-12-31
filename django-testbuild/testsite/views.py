from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import PasswordEntry
from .forms import PasswordEntryForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def create_password_entry(request):
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            request.session['form_data'] = form.cleaned_data
            return redirect('review_password_entry')
    else:
        input_data = request.session.pop('form_data', None)
        if input_data:
            form = PasswordEntryForm(initial=input_data)
        else:
            form = PasswordEntryForm()
    return render(request, 'create_password_entry.html', {'form': form})

@login_required
def preview_password_entry(request):
    if 'form_data' not in request.session:
        return redirect('create_password_entry') # Redirect if no data is in session

    if request.method == 'POST':
        if 'confirm' in request.POST.getlist('action'):
            # User confirmed, save the data
            form_data = request.session['form_data']
            form = PasswordEntryForm(form_data)
            if form.is_valid():
                form.save()
                del request.session['form_data'] # Clear data from session
                messages.success(request, 'Submission successful!')
                return redirect('confirm_password_entry')
        elif 'edit' in request.POST.getlist('action'):
            # User wants to edit, redirect back to form
            return render(request, 'create_password_entry.html', {'form': request.session['form_data']})
        else:
            # Handle error if data somehow became invalid
            messages.error(request, 'An error occurred during save.')
            return redirect('create_password_entry')
            
    # For GET request, display the data for review
    return render(request, 'review_password_entry.html', {'form': request.session['form_data']})

@login_required
def confirm_password_entry(request):
    return render(request, 'confirm_password_entry.html')

@login_required
def show_password_entries(request):
    entries = PasswordEntry.objects.all()
    return render(request, 'show_password_entries.html', {'entries': entries})


