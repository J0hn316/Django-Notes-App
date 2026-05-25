from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .models import Note
from .forms import NoteForm


def notes_home(request):
    query = request.GET.get("q", "")
    page_number = request.GET.get("page", 1)

    notes = Note.objects.all().order_by("-created_at")

    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))

    paginator = Paginator(notes, 5)
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "query": query,
    }

    return render(request, "notes/notes_home.html", context)


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save()
            messages.success(request, "Note created successfully.")
            return redirect("note_detail", pk=note.pk)

    else:
        form = NoteForm()

    context = {"form": form, "page_title": "Create Note", "button_text": "Save Note"}

    return render(request, "notes/note_form.html", context)


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    context = {"note": note}

    return render(request, "notes/note_detail.html", context)


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully.")
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)

    context = {
        "form": form,
        "page_title": "Edit Note",
        "button_text": "Update Note",
    }

    return render(request, "notes/note_form.html", context)


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        messages.success(request, "Note deleted successfully.")
        return redirect("notes_home")

    context = {"note": note}

    return render(request, "notes/note_confirm_delete.html", context)
