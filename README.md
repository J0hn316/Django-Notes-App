# Django Notes App

A beginner-friendly Django web application for creating, managing, searching, and organizing private notes by user account.

This project was built to practice Django fundamentals, including models, migrations, templates, class-based views, authentication, user-owned data, pagination, search, admin customization, and automated testing.

## Features

- User registration
- User login and logout
- Create notes
- View all notes
- View a single note
- Edit notes
- Delete notes with confirmation
- Search notes by title or content
- Paginate notes
- Flash success messages after create, update, and delete actions
- User-owned notes, so each user only sees their own data
- Django admin support for managing notes
- Automated tests for important app behavior

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```txt
django-notes-app/
├── accounts/
├── config/
├── notes/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/django-notes-app.git
cd django-notes-app
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Then open:

```txt
http://127.0.0.1:8000/
```

The root URL redirects to:

```txt
http://127.0.0.1:8000/notes/
```

## Running Tests

Run:

```bash
python manage.py test
```

## Main URLs

```txt
/                         Redirects to notes list
/notes/                   Notes list
/notes/create/            Create note
/notes/<id>/              Note detail
/notes/<id>/edit/         Edit note
/notes/<id>/delete/       Delete note
/accounts/register/       Register
/accounts/login/          Login
/accounts/logout/         Logout
/admin/                   Django admin
```

## What I Learned

While building this project, I practiced:

- Creating a Django project and app
- Defining models and running migrations
- Using Django templates and template inheritance
- Creating reusable forms with `ModelForm`
- Using Django class-based views
- Protecting routes with `LoginRequiredMixin`
- Connecting notes to the logged-in user with a `ForeignKey`
- Filtering database queries by authenticated user
- Adding search with `Q` objects
- Adding pagination with Django’s `Paginator`
- Showing success messages with Django’s messages framework
- Customizing the Django admin panel
- Writing automated tests with Django’s `TestCase`
