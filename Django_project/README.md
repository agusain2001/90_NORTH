# Django Chat Application

## **Features**
1. **User Management**:
   - Users can sign up and log in securely.
   - Login credentials are validated and stored in the database.

2. **Real-Time Chat**:
   - Chat messages are exchanged using WebSocket for seamless real-time communication.

3. **User-Friendly Interface**:
   - A collapsible left menu displays all registered users.
   - Clean and responsive UI for a modern chatting experience.

4. **Message Persistence**:
   - All chat messages are stored in the database for future retrieval.
   - Old messages are loaded and displayed when chatting with a user.

5. **Responsive Design**:
   - The layout adapts to various screen sizes, offering an optimal user experience on both desktop and mobile devices.

---

## **How to Run Locally**

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd django-chat-application
   ```

2. **Install Dependencies**:
   Ensure you have Python 3 and pip installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**:
   Run migrations to set up the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## **Hosting Information**

### **Live Server**
The application is currently hosted on PythonAnywhere and can be accessed at:
- [Django Chat Application Live Server](http://agusain.pythonanywhere.com/)

### **Run Locally and Hosted**
This project is functional both locally on your development server and hosted on PythonAnywhere.

---

## **Folder Structure**
```
├── chat_app/                    # Main Django app folder
│   ├── migrations/             # Database migrations
│   ├── static/                 # Static files (CSS, JS, Images)
│   ├── templates/              # HTML templates
│   ├── views.py                # Application logic
│   ├── models.py               # Database models
│   └── urls.py                 # URL configurations
├── manage.py                   # Django project manager
├── db.sqlite3                  # SQLite database file
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## **Features to Enhance**
1. Add support for media (image, video) sharing in chat.
2. Implement group chat functionality.
3. Enhance the authentication process with email verification.

---

## **Submission Guidelines**
- Ensure that the repository is updated with all necessary files.
- Include this `README.md` in the root directory.
- Host the project on PythonAnywhere or AWS and provide the live server link.
- Share the GitHub repository link and live server URL as per the assignment requirements.

---

For any questions or issues, feel free to contact us!
