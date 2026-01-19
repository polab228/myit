# ITMO University Personal Account Replica

This project is a Django-based web application that replicates the personal account system of ITMO University. It includes features such as user authentication, a dashboard, and various pages for grades, schedules, finances, and electives.

## Project Structure

```
itmo_replica/
├── manage.py                # Command-line utility for interacting with the Django project
├── itmo_replica/            # Main project directory
│   ├── __init__.py          # Indicates that this directory should be treated as a Python package
│   ├── settings.py          # Configuration settings for the Django project
│   ├── urls.py              # URL routing for the project
│   ├── wsgi.py              # Entry point for WSGI-compatible web servers
│   └── asgi.py              # Entry point for ASGI-compatible web servers
├── accounts/                 # Application for user accounts
│   ├── __init__.py          # Indicates that this directory should be treated as a Python package
│   ├── admin.py             # Admin interface registration for models
│   ├── apps.py              # Configuration for the accounts application
│   ├── models.py            # Data models for user authentication
│   ├── tests.py             # Tests for the accounts application
│   ├── views.py             # View functions for handling requests
│   ├── urls.py              # URL routing specific to the accounts application
│   ├── templates/           # HTML templates for the accounts application
│   │   └── accounts/
│   │       ├── login.html   # Login page template
│   │       ├── dashboard.html# User dashboard template
│   │       ├── grades.html   # Grades page template
│   │       ├── schedule.html  # Schedule page template
│   │       ├── finances.html  # Finances page template
│   │       └── electives.html # Electives page template
│   └── static/              # Static files (CSS, JS) for the accounts application
│       └── accounts/
│           ├── css/
│           │   ├── style.css        # Main CSS styles
│           │   ├── line.css         # Additional CSS styles
│           │   └── solid.css        # CSS for solid elements
│           └── js/
│               ├── layout-helpers.js # JavaScript for layout management
│               └── tag.js           # JavaScript for handling tags
├── requirements.txt          # Required Python packages for the project
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd itmo_replica
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install requirements**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Create a superuser** (for accessing the admin interface):
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```
   python manage.py runserver
   ```

7. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/accounts/login/` to access the login page.

## Features123123

- User authentication with a simple login page.
- Dashboard for users after logging in.
- Pages for grades, schedules, finances, and electives.
- Static files for CSS and JavaScript to ensure visual fidelity to the original ITMO University site.

## Restrictions

This project can be configured to restrict access based on geographical regions. Further implementation details can be found in the `settings.py` file.

## License

This project is open-source and available for modification and distribution under the MIT License.