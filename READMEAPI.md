# Django User Management and Task Tracking API

## Overview

This Django REST framework API provides features for user management, app creation, task tracking, authentication, and authorization. The API is designed for creating and managing users, apps, and tasks in a comprehensive manner.

## Installation

1\. **Clone the repository:**

```plaintext\
   git clone https://github.com/devPrasanthKumar/user-management-and-task-tracking.git
  

python -m venv venv\\
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

## API Endpoints\

### User Authentication

#### User Registration


-   Method - POST
-   **Endpoint:** /register/\
-   Users can create an account by providing a username, email, and password.\
-   Passwords are validated for strength.

#### User Login

-   Method - POST
-   **Endpoint:** /login/\
-   Users can log in with their email and password.\
-   If already logged in, users are redirected to the home page.

#### User Logout

-   Method - POST
-   **Endpoint:** /logout/\
-   Users can log out, and they are redirected to the login page.

### User Management

#### Update User Profile


-   Method - (PUT) OR (PATCH)
-   **Endpoint:** /showuserprofile/<uuid:pk>\
-   Users can update their profile information, such as username and email.

#### View User Profile

- Method - GET
-   **Endpoint:** /showuserprofile/<uuid:pk>/\
-   Users can view their user profile details.

### App Management

#### Create App

-   Method - POST
-   **Endpoint:** /addapp/\
-   Administrators can create new apps by providing details such as app name, link, category, and sub-category.

#### Update App

-   Method - PUT
-   **Endpoint:** /addapp/<int:pk>\
-   Administrators can update exisiting app's details such as app name, link, category, and sub-category.

#### Update App


-   Method - PATCh
-   **Endpoint:** /addapp/<int:pk>\
-   Administrators can partially update exisiting app's details such as app name, link, category, and sub-category.

#### Delete App

-   Method - DELETE
-   **Endpoint:** /addapp/<int:pk>\
-   Administrators can delete exisiting app by id.

####  View all App  (for User)

-   Method - GET
-   **Endpoint:** /showappsforuser/\
-   Users can view all app, including its name, link, and category.

####  View a app Details (for User)

-   Method - GET
-   **Endpoint:** /showappsforuser/<int:pk>\
-   Users can view details about a particular app, including its name, link, and category.

### Task Tracking

#### Upload Task

-   Method - POST
-   **Endpoint:** /task/int:pk/\
-   Users can upload a task image for a specific app.

#### View Completed Tasks

-   Method - GET
-   **Endpoint:** /task/<int:pk>/\
-   Users can view a list of tasks they have completed.

#### View User Points

-   Method - GET
-   **Endpoint:** /userpoints/\
-   Users can view their total points earned from completed tasks.

## Models\

### UserProfileModel

Represents user profile details such as username, email, and points.

### AndroidAppModel

Represents app details, including name, link, category, sub-category, and points.

### TaskModel

Represents uploaded tasks, associated with a user and an app.

### User (Custom)

Custom user model extending AbstractUser to include a role field (Admin or Normal User).

## Serializers\

### TaskSerializer

Serializer for the TaskModel.

### AndroidAppSerializer

Serializer for the AndroidAppModel.

### UserPointSerializer

Serializer for calculating and displaying user points.

### UserAccountCreateSerializer

Serializer for user registration, login, and logout.

### UserProfileSerializer

Serializer for displaying user profile details.

## Custom Permissions\

### AdminCanAccess

Custom permission allowing only admin users to access certain views.

## Swagger Documentation\

-   **Endpoint:** /swagger/\
-   API documentation using Swagger for easy reference.

`
```
