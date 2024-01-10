Django User Management and Task Tracking System

This Django project serves as a comprehensive user management system with features like user registration, login, logout, user profile management, app creation, task tracking, and more. The system is designed to allow administrators to create and manage apps, while normal users can interact with the platform by uploading tasks and tracking their points.\

website : https://new-task-tracker.onrender.com/

Table of Contents

Installation\
    User Authentication\
    User Management\
    App Management\
    Task Tracking\
    Models\
    Forms\
    Authors

Installation

Clone the repository:

bash

git clone https://gitlab.com/devPrasanthKumar/task-trackerr.git

Create and activate a virtual environment:

python -m venv venv\
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

Open your browser and navigate to http://localhost:8000/

User Authentication\
User Registration

Endpoint: /createaccount/\
    Users can create an account by providing a username, email, and password.\
    Passwords are validated for strength.

User Login

Endpoint: /\
    Users can log in with their email and password.\
    If already logged in, users are redirected to the home page.

User Logout

Endpoint: /logout/\
    Users can log out, and they are redirected to the login page.

User Management\
Update User Profile

Endpoint: /updateprofile/<uuid:pk>\
    Users can update their profile information, such as username and email.

View User Profile

Endpoint: /userprofile/<uuid:pk>/\
    Users can view their user profile details.

App Management\
Create App

Endpoint: /main/home/\
    Administrators can create new apps by providing details such as app name, link, category, and sub-category.

View App Details

Endpoint: /main/singledata/<int:pk>/\
    Users can view details about a particular app, including its name, link, and category.

View Completed Tasks

Endpoint: /main/showcompletedtask/\
    Users can view a list of tasks they have completed.

View User Points

Endpoint: /main/showpoints/\
    Users can view their total points earned from completed tasks.

Models\
UserProfileModel

Represents user profile details such as username, email, and points.

AndroidAppModel

Represents app details, including name, link, category, sub-category, and points.

TaskModel

Represents uploaded tasks, associated with a user and an app.

User (Custom)

Custom user model extending AbstractUser to include a role field (Admin or Normal User).

Forms\
CreateAppForm

Form for creating a new app by administrators.

UploadTaskForm

Form for users to upload a task image.

UpdateUserProfileForm

Form for users to update their profile information.

AccountCreateForm

Form for user registration.

UpdateUserForm

Form for updating user information.

Signal\
Automatic Profile Creation

A signal has been implemented to automatically create a user profile when a user account is created

Authors

prasanthkumar\
    Email: prasanth52010@gmail.com
