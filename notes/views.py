from django.shortcuts import render, redirect
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
            form.save()
            return redirect("notes_home")

    else:
        form = NoteForm()

    context = {"form": form}

    return render(request, "notes/note_form.html", context)
