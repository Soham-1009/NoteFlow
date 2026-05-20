

```
# ✦ Noteflow — Django + MySQL Notes App

A full-featured notes-taking web application built to help you capture and organize your thoughts easily.

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
| **🏷️ Categories** | Organize notes by Personal, Work, Ideas, To-Do, or Other. |
| **🔍 Smart Search** | Fast search that waits until you stop typing and keeps your cursor in place. |
| **🔽 Filter** | Easily filter notes by picking a category from the dropdown menu. |
| **📊 Quick Stats** | See your total notes and pinned count right at the top. |

---

## 📁 Project Structure

```text
Noteflow/
├── .gitignore            
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

## Requirements

## 🚀 Setup Instructions

### Step 1 — Set Up MySQL Database
Open your MySQL shell in your terminal:
```bash
mysql -u root -p
```
Then run your SQL setup script to create the database:
```bash
mysql -u root -p < setup_mysql.sql
```

### Step 2 — Create a Virtual Environment
```bash
# Go to the main project folder
cd Noteflow

# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```

### Step 3 — Install Required Packages
```bash
pip install -r requirements.txt
```
> **Windows tip**: If `mysqlclient` gives you an error, try running `pip install mysql-connector-python` and change your `settings.py` database ENGINE to `'mysql.connector.django'`.

### Step 4 — Connect the Database
Open `src/notes_project/settings.py` and put your MySQL details in the `DATABASES` section:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'notes_db',           
        'USER': 'root',               
        'PASSWORD': 'your_password',  
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Step 5 — Make the Database Tables
```bash
# Go inside the code folder
cd src

# Run the migrations
python manage.py makemigrations
python manage.py migrate
```

### Step 6 — Start the App
```bash
python manage.py runserver
```
Open your web browser and visit: **http://127.0.0.1:8000**

---

## 🗄️ Database Tables

### `auth_user` (Made by Django)
Holds user accounts (`id`, `username`, `email`, `password`).

### `notes_app_note` (Made by us)
Holds your notes. 
- `user_id`: Links to the user who made the note.
- `title`, `content`, `category`, `is_pinned`: The details of the note.
- `created_at`, `updated_at`: The exact times the note was made and last changed.

---

## 💡 Production Tips
If you put this app on the live internet:
1. Change `DEBUG = True` to `DEBUG = False` in your `settings.py` file.
2. Hide your `SECRET_KEY` using environment variables.
3. Put your real website name in `ALLOWED_HOSTS`.
4. Run `python manage.py collectstatic` to gather your CSS files.
```
