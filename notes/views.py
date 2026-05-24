from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def notes_home(request):
    notes = Note.objects.all().order_by("-created_at")

    context = {"notes": notes}

    return render(request, "notes/notes_home.html", context)


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save()
            return redirect("notes_detail", pk=note.pk)

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
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)

    context = {
        "form": form,
        "page_title": "Edit Note",
        "button_text": "Update Note",
    }

    return render(request, "notes/note_form.html", context)
