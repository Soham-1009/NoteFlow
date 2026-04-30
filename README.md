# ✦ NoteFlow — Django + MySQL Notes App

A full-featured notes-taking web application built with:
- **Frontend**: Plain HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: MySQL

---

## 📁 Project Structure

```
# ✦ NoteFlow — Django + MySQL Notes App

A full-featured notes-taking web application built to help you capture and organise your thoughts easily. 

**Author:** Soham Santosh Deshpande

---

## 🛠️ Tech Stack
- **Frontend:** Plain HTML, CSS, Vanilla JavaScript
- **Backend:** Django (Python 3.10+)
- **Database:** MySQL 8.0+

---

## 🌟 Features

| Feature | Description |
|---|---|
| **🔐 User Authentication** | Secure register, login, and logout. Users can only see their own notes. |
| **📝 Create Notes** | Add a title, write your thoughts, pick a category, and pin it to the top. |
| **✏️ Edit Notes** | Change any note at any time. |
| **🗑️ Delete Notes** | Shows a warning screen first to stop accidental deletes. |
| **📌 Pin Notes (AJAX)** | Pin important notes to the top instantly without reloading the page. |
| **🏷️ Categories** | Organise notes by Personal, Work, Ideas, To-Do, or Other. |
| **🔍 Smart Search** | Fast search that waits until you stop typing (debounced) and keeps your typing cursor in place. |
| **🔽 Filter** | Easily filter notes by picking a category from the dropdown. |
| **📊 Quick Stats** | See your total notes and pinned count right at the top. |

---

## 📁 Project Structure

```text
Noteflow/                
├── requirements.txt
├── setup_mysql.sql
├── README.md
└── src/
    ├── manage.py
    ├── notes_project/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── notes_app/
        ├── models.py
        ├── views.py
        ├── forms.py
        ├── urls.py
        └── templates/
            └── notes_app/
                ├── base.html
                ├── login.html
                ├── register.html
                ├── home.html
                ├── note_form.html
                ├── note_detail.html
                └── confirm_delete.html
```

---

## ⚙️ Prerequisites

Make sure you have these installed:
- Python 3.10+
- MySQL 8.0+
- pip

---

## 🚀 Setup Instructions

### Step 1 — Set Up MySQL Database

Open your MySQL shell:
```bash
mysql -u root -p
```

Then run the SQL setup script:
```bash
mysql -u root -p < setup_mysql.sql
```

Or paste the contents of `setup_mysql.sql` manually into the MySQL shell.

---

### Step 2 — Create a Virtual Environment

```bash
# Navigate to the project folder
cd notes_app

# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note for Windows users**: If `mysqlclient` fails to install, try:
> ```bash
> pip install mysqlclient --only-binary=mysqlclient
> ```
> Or install MySQL Connector as an alternative:
> ```bash
> pip install mysql-connector-python
> ```
> Then update `settings.py` ENGINE to: `'mysql.connector.django'`

---

### Step 4 — Configure Database Settings

Open `notes_project/notes_project/settings.py` and update the `DATABASES` section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'notes_db',           # Database name from setup_mysql.sql
        'USER': 'notes_user',         # MySQL username
        'PASSWORD': 'your_strong_password',  # MySQL password you set
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### Step 5 — Run Migrations

```bash
cd notes_project

# Create the database tables
python manage.py makemigrations
python manage.py migrate
```

---

### Step 6 — Create an Admin Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### Step 7 — Start the Development Server

```bash
python manage.py runserver
```

Open your browser and go to: **http://127.0.0.1:8000**

---

## 🌟 Features

| Feature | Description |
|---|---|
| 🔐 User Authentication | Register, Login, Logout with session management |
| 📝 Create Notes | Add title, content, category, and pin status |
| ✏️ Edit Notes | Update any note at any time |
| 🗑️ Delete Notes | With confirmation prompt to avoid accidents |
| 📌 Pin Notes | Pin important notes to the top (via AJAX, no page reload) |
| 🏷️ Categories | Personal, Work, Ideas, To-Do, Other |
| 🔍 Search | Real-time debounced search across title and content |
| 🔽 Filter | Filter notes by category |
| 📊 Stats | See total notes and pinned count at a glance |

---

## 🗄️ Database Schema

### `auth_user` (Django built-in)
| Column | Type |
|---|---|
| id | INT (PK) |
| username | VARCHAR |
| email | VARCHAR |
| password | VARCHAR (hashed) |

### `notes_app_note`
| Column | Type | Description |
|---|---|---|
| id | INT (PK, auto) | Primary key |
| user_id | INT (FK) | References auth_user |
| title | VARCHAR(255) | Note title |
| content | TEXT | Note body |
| category | VARCHAR(20) | personal/work/ideas/todo/other |
| is_pinned | BOOLEAN | Pinned to top |
| created_at | DATETIME | Auto set on creation |
| updated_at | DATETIME | Auto updated on save |

---

## 🔗 URL Routes

| URL | View | Description |
|---|---|---|
| `/` | home_view | Dashboard with all notes |
| `/register/` | register_view | Create new account |
| `/login/` | login_view | Log in |
| `/logout/` | logout_view | Log out |
| `/notes/create/` | create_note_view | New note form |
| `/notes/<id>/` | detail_note_view | View a note |
| `/notes/<id>/edit/` | edit_note_view | Edit a note |
| `/notes/<id>/delete/` | delete_note_view | Delete confirmation |
| `/notes/<id>/pin/` | toggle_pin_view | AJAX pin toggle |
| `/admin/` | Django admin | Admin panel |

---

## 🛠️ Troubleshooting

**`mysqlclient` install error on Windows**
Install MySQL C connector first from: https://dev.mysql.com/downloads/connector/c/

**`django.db.utils.OperationalError: (1045, "Access denied")`**
Double-check your MySQL username/password in `settings.py`

**`No module named 'notes_app'`**
Make sure you're running commands from inside the `notes_project/` folder (where `manage.py` lives)

**Templates not found**
Ensure `'APP_DIRS': True` is set in `TEMPLATES` in `settings.py` (it is by default)

---

## 📌 Production Tips

- Set `DEBUG = False` in `settings.py`
- Move `SECRET_KEY` to an environment variable
- Set `ALLOWED_HOSTS` to your domain
- Use `python manage.py collectstatic` for static files
- Use Gunicorn + Nginx for serving the app
