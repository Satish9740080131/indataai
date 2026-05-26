# InDataAI Clone — Django + MySQL

A full clone of [indataai.in](https://indataai.in) built with Django, HTML, CSS, JS, and MySQL.

## Project Structure

```
indataai[clone]/
├── indataai_clone/         # Django project config (settings, urls, wsgi)
├── website/                # Main Django app
│   ├── migrations/
│   ├── templates/
│   │   └── website/        # All HTML templates live here (app-level)
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/style.css
│   ├── img/
│   └── js/main.js
├── media/                  # Uploaded files (gitignored)
├── scripts/                # Utility scripts (run from project root)
│   ├── create_db.py
│   ├── seed_data.py
│   └── append_css.py
├── manage.py
└── README.md
```

## Setup

### 1. Create the MySQL database
```
python scripts/create_db.py
```

### 2. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a superuser
```
python manage.py createsuperuser
```

### 4. Seed sample data
```
python scripts/seed_data.py
```

### 5. Run the development server
```
python manage.py runserver
```

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Pages

| URL              | Page        |
|------------------|-------------|
| `/`              | Home        |
| `/about/`        | About Us    |
| `/services/`     | Services    |
| `/faq/`          | FAQ         |
| `/portfolio/`    | Portfolio   |
| `/event/`        | Events      |
| `/client/`       | Testimonials|
| `/contact/`      | Contact     |
| `/request-quote/`| Get a Quote |
