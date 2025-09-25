User Authentication Service 🚀

This project is a user authentication service built with Flask and SQLAlchemy. It provides a foundational backend system for handling user registration, login, session management, and password resets. The architecture emphasizes a clean separation of concerns, ensuring the web layer is decoupled from the database logic.

Learning Objectives 🧠

By the end of this project, you will be able to explain and implement the following concepts:

    How to declare API routes in a Flask application.

    How to get and set cookies for session management.

    How to retrieve and process request form data.

    How to use SQLAlchemy as an ORM to interact with a database.

    How to return appropriate HTTP status codes from an API.

    How to securely hash passwords and manage user credentials.

Requirements 🛠️

    OS: Ubuntu 20.04 LTS

    Python: Version 3.9

    PIP for Python 3

    Editors: vi, vim, or emacs

Setup and Installation ⚙️

Follow these steps to get the project up and running on your local machine.

    Clone the repository:
    Bash

git clone <your_repository_url>

Navigate to the project directory:
Bash

cd atlas-web_back_end/user_authentication_service

Install the required Python packages:
Bash

pip3 install Flask SQLAlchemy bcrypt

Make all Python files executable:
This is a project requirement to ensure all scripts can be run directly.
Bash

    chmod +x *.py

File Descriptions 📁

    user.py: Defines the User data model using SQLAlchemy, which maps to the users table in the database.

    db.py: (To be created) Contains the DB class responsible for all direct database interactions and session management.

    auth.py: (To be created) Implements the Auth class, which handles the business logic for authentication (e.g., registering users, validating logins).

    app.py: (To be created) The main Flask application file that defines all API endpoints and handles HTTP requests and responses.