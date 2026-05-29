from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTests(TestCase):
    def test_note_string_returns_title(self):
        user = get_user_model().objects.create_user(
            username="john",
            password="testpass123",
        )

        note = Note.objects.create(
            user=user,
            title="Test Note",
            content="This is a test note.",
        )

        self.assertEqual(str(note), "Test Note")


class NoteViewTests(TestCase):
    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="john",
            password="testpass123",
        )

        self.other_user = User.objects.create_user(
            username="jane",
            password="testpass123",
        )

        self.note = Note.objects.create(
            user=self.user,
            title="John Note",
            content="This note belongs to John.",
        )

        self.other_note = Note.objects.create(
            user=self.other_user,
            title="Jane Note",
            content="This note belongs to Jane.",
        )

    def test_notes_list_requires_login(self):
        response = self.client.get(reverse("notes_home"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_logged_in_user_can_view_notes_list(self):
        self.client.login(username="john", password="testpass123")

        response = self.client.get(reverse("notes_home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Note")

    def test_user_only_sees_their_own_notes(self):
        self.client.login(username="john", password="testpass123")

        response = self.client.get(reverse("notes_home"))

        self.assertContains(response, "John Note")
        self.assertNotContains(response, "Jane Note")

    def test_user_can_view_their_own_note_detail(self):
        self.client.login(username="john", password="testpass123")

        response = self.client.get(reverse("note_detail", kwargs={"pk": self.note.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Note")

    def test_user_cannot_view_another_users_note_detail(self):
        self.client.login(username="john", password="testpass123")

        response = self.client.get(
            reverse("note_detail", kwargs={"pk": self.other_note.pk})
        )

        self.assertEqual(response.status_code, 404)

    def test_logged_in_user_can_create_note(self):
        self.client.login(username="john", password="testpass123")

        response = self.client.post(
            reverse("note_create"),
            {
                "title": "New Note",
                "content": "This note was created in a test.",
            },
        )

        self.assertEqual(response.status_code, 302)

        new_note = Note.objects.get(title="New Note")

        self.assertEqual(new_note.user, self.user)
        self.assertEqual(new_note.content, "This note was created in a test.")

    def test_search_notes_by_title(self):
        self.client.login(username="john", password="testpass123")

        response = self.client.get(reverse("notes_home"), {"q": "John"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Note")

    def test_search_does_not_show_other_users_notes(self):
        self.client.login(username="john", password="testpass123")

        response = self.client.get(reverse("notes_home"), {"q": "Jane"})

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Jane Note")
