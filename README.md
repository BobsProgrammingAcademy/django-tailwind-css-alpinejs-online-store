# Online Store

This is an online store built using **Django 5**, **Tailwind CSS**, and **Alpine.js**.

![plot](https://github.com/BobsProgrammingAcademy/django-tailwind-css-alpinejs-online-store/blob/master/static/img/store.png?raw=true)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the application](#run-the-application)
- [View the application](#view-the-application)
- [Add data to the application](#add-data-to-the-application)
- [Copyright and License](#copyright-and-license)

### Prerequisites

Install the following prerequisites:

1. [Python 3.10-3.12](https://www.python.org/downloads/)
   <br> This project uses **Django v5.0.2**. For Django to work, you must install a correct version of Python on your machine. More information [here](https://django.readthedocs.io/en/stable/faq/install.html).
2. [Node.js](https://nodejs.org/en/)
3. [Visual Studio Code](https://code.visualstudio.com/download)

### Installation

#### 1. Create a virtual environment

From the **root** directory, run:

```bash
python -m venv venv
```

#### 2. Activate the virtual environment

From the **root** directory, run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

#### 3. Install required dependencies

From the **root** directory, run:

```bash
pip install -r requirements.txt
```

#### 4. Run migrations

From the **root** directory, run:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

#### 5. Create an admin user to access the Django Admin interface

From the **root** directory, run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.

#### 6. Install required frontend dependencies

From the **root** directory, run:

```bash
npm install
```

### Run the application

From the **root** directory, run:

```bash
python manage.py runserver
```

### View the application

Go to http://127.0.0.1:8000/ to view the application.

### Add data to the application

Add data through Django Admin.

Go to http://127.0.0.1:8000/admin to access the Django Admin interface and sign in using the admin credentials.

### Copyright and License

Copyright © 2024 Bob's Programming Academy. Code released under the MIT license.
