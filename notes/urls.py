from django.urls import path

from . import views

urlpatterns = [
    path("", views.notes_home, name="notes_home"),
    path("create/", views.note_create, name="note_create"),
]
