## Documentation (README.md)

# Django Chat Application

## Features
1. User signup and login functionality.
2. Display all registered users in a collapsible left menu.
3. Initiate chat with any user and store chat messages in the database.
4. Retrieve and display old messages in the chat interface.
5. WebSocket-based real-time communication.
6. Modern UI/UX design with a responsive layout.

## How to Run
1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Make migrations and migrate:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Run the development server:
    ```bash
    python manage.py runserver
    ```
5. Open the browser and navigate to `http://127.0.0.1:8000/`.

## Hosting
The project can be hosted on PythonAnywhere or AWS. Refer to the submission guidelines for links and steps.








