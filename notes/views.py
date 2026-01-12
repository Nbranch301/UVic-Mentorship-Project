from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Note
from .forms import NoteForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required
def home(request):
    latest_notes_list = Note.objects.filter(owner=request.user).order_by("-modified")
    context = {"latest_notes_list": latest_notes_list}
    return render(request, "notes/home.html", context)

@login_required
def edit(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)

    # Check if user is submitting form
    if request.method == 'POST':
        
        # Create new form with user's submitted data
        form = NoteForm(request.POST, instance=note)
        
         # If data is valid, save info to database
        if form.is_valid():
            form.save()
            messages.success(request, 'Your note was saved')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/form.html', {'form': form, 'note_id': note_id})

@login_required
def create(request):
    new_note = Note.objects.create(title='Untitled', text='', owner=request.user)
    return redirect('notes:edit', note_id=new_note.id)

@login_required
@require_POST
def delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    note.delete()
    return redirect('notes:home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notes:home')
    else:
        form = SignUpForm()
    return render(request, 'notes/signup.html', {'form': form})