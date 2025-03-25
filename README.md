# Task Management API

## Complete Setup & Usage Guide


# Run these commands one after another:
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

API Documentation

Access interactive docs at:
http://localhost:8000/swagger/

API Endpoints
User Authentication

POST /register/
{
  "username": "your_username",
  "password": "your_password"
}

POST /login/
{
  "username": "your_username",
  "password": "your_password"
}
Returns: {"token": "abc123", "user_id": 1}

Task Management

POST /tasks/
{
  "title": "Task title",
  "content": "Task details",
  "status": "pending"
}

GET /tasks/ 
Returns all your tasks

PATCH /tasks/1/
{
  "status": "completed"
}

Included Files

swagger.json - Full API documentation
