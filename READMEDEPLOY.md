# Task Tracker Project

This project is a Task Tracker application deployed on [Render](https://render.com/).

## Overview

The Task Tracker allows users to manage and track their tasks efficiently. The application is deployed using the Render free web service, making it accessible without the need for personal servers.

## Deployment on Render

### Prerequisites

- GitLab account
- Render account

### Deployment Steps

1. **Push Folder to the Repository:**

   ```bash

   git init
   git add .
   git commit -m "new comit"
   git remote add origin https://gitlab.com/devPrasanthKumar/task-trackerr.git
   git push origin main

   ```

2. **Configure Render:**

   - Create an account on [Render](https://render.com/).
   - Set up a new web service on Render, connecting it to your GitLab repository.

3. **Configure Render :**

   - Enter App Name
   - Choose the server
   - gunicorn taskProjectApp.wsgi
   - Add environment variables on Render:
     - `SECRET_KEY`: `<my_secret_key>`
     - `DEBUG`: `False` (for production,need to setup this on django's settings.py)
     - `ALLOWED_HOSTS: ["*"]` (for production , need to setup this on django's settings.py)

4. **Database:**

   - here i used the default db (sqlite3).

5. **Push Changes to GitLab:**

   ```bash
   git add .
   git commit -m "Deploy on Render"
   git push origin main
   ```

6. **Access Your Deployed App:**

   Once the deployment is complete, your Task Tracker application will be accessible at the provided Render URL.

## Local Development

If you want to run the project locally:

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

3. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://localhost:8000/`.

Authors

prasanthkumar\
