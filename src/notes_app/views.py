from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import Note
from .forms import RegisterForm, LoginForm, NoteForm


# ─── Auth Views ──────────────────────────────────────────────────────────────

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'notes_app/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)
                
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'notes_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


# ─── Notes Views ─────────────────────────────────────────────────────────────

@login_required
def home_view(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    notes = Note.objects.filter(user=request.user)

    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if category:
        notes = notes.filter(category=category)

    categories = Note.CATEGORY_CHOICES
    total_notes = Note.objects.filter(user=request.user).count()
    pinned_count = Note.objects.filter(user=request.user, is_pinned=True).count()

    context = {
        'notes': notes,
        'query': query,
        'selected_category': category,
        'categories': categories,
        'total_notes': total_notes,
        'pinned_count': pinned_count,
    }
    return render(request, 'notes_app/home.html', context)


@login_required
def create_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note created successfully!')
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes_app/note_form.html', {'form': form, 'action': 'Create'})


@login_required
def edit_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes_app/note_form.html', {'form': form, 'action': 'Edit', 'note': note})


@login_required
def delete_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted.')
        return redirect('home')
    return render(request, 'notes_app/confirm_delete.html', {'note': note})


@login_required
def detail_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'notes_app/note_detail.html', {'note': note})


@login_required
@require_POST
def toggle_pin_view(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.is_pinned = not note.is_pinned
    note.save()
    return JsonResponse({'pinned': note.is_pinned})
