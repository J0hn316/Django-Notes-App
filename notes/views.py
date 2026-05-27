from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Note
from .forms import NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/notes_home.html"
    context_object_name = "notes"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("q", "")

        notes = Note.objects.filter(user=self.request.user).order_by("-created_at")

        if query:
            notes = notes.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )

        return notes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Note created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Note"
        context["button_text"] = "Save Note"
        return context


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Note updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Edit Note"
        context["button_text"] = "Update Note"
        return context


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    context_object_name = "note"
    success_url = reverse_lazy("notes_home")

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Note deleted successfully.")
        return super().form_valid(form)
