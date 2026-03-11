```markdown
# CodeCraftHub

## 1. Project Overview and Description

CodeCraftHub is a simple personalized learning platform built using Python and the Flask framework. The purpose of this project is to help developers keep track of courses they want to learn. Users can add courses, update their progress, view all tracked courses, and delete courses when they are no longer needed.

This project is designed for beginners who are learning REST APIs. Instead of using a database, course information is stored in a JSON file. This keeps the project simple and helps learners focus on understanding REST API concepts such as HTTP methods, endpoints, and CRUD operations.

---

# 2. Features List

- Track courses you want to learn
- Create, read, update, and delete course records
- Store course data in a JSON file
- Automatic ID generation for each course
- Automatic creation timestamp for courses
- Input validation for required fields
- Validation for course status values
- Error handling for missing or invalid data
- Beginner-friendly REST API structure

---

# 3. Installation Instructions (Step-by-Step)

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

Check installation:

```

python --version

```

---

### Step 2: Create a Project Folder

```

mkdir CodeCraftHub
cd CodeCraftHub

```

---

### Step 3: Create the Application File

Create a file named:

```

app.py

```

Paste the Flask application code into this file.

---

### Step 4: Install Flask

Install Flask using pip:

```

pip install flask

```

---

### Step 5: Prepare the JSON Data File

The application automatically creates the file if it does not exist.

You may also create it manually:

```

courses.json

```

Initial content:

```

[]

```

---

# 4. How to Run the Application

Run the application using:

```

python app.py

```

The Flask server will start and display something similar to:

```

Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)

```

The API will now be available at:

```

[http://127.0.0.1:5000](http://127.0.0.1:5000)

```

---

# 5. API Endpoints Documentation with Examples

## Add a New Course

Endpoint

```

POST /api/courses

```

Example request:

```

curl -X POST [http://127.0.0.1:5000/api/courses](http://127.0.0.1:5000/api/courses) 
-H "Content-Type: application/json" 
-d '{
"name": "Flask REST API",
"description": "Learn how to build REST APIs with Flask",
"target_date": "2026-04-10",
"status": "Not Started"
}'

```

Example response:

```

{
"id": 1,
"name": "Flask REST API",
"description": "Learn how to build REST APIs with Flask",
"target_date": "2026-04-10",
"status": "Not Started",
"created_at": "2026-03-11T19:00:00"
}

```

---

## Get All Courses

Endpoint

```

GET /api/courses

```

Example request:

```

curl [http://127.0.0.1:5000/api/courses](http://127.0.0.1:5000/api/courses)

```

Example response:

```

[
{
"id": 1,
"name": "Flask REST API",
"description": "Learn how to build REST APIs with Flask",
"target_date": "2026-04-10",
"status": "Not Started",
"created_at": "2026-03-11T19:00:00"
}
]

```

---

## Get a Specific Course

Endpoint

```

GET /api/courses/<id>

```

Example request:

```

curl [http://127.0.0.1:5000/api/courses/1](http://127.0.0.1:5000/api/courses/1)

```

---

## Update a Course

Endpoint

```

PUT /api/courses/<id>

```

Example request:

```

curl -X PUT [http://127.0.0.1:5000/api/courses/1](http://127.0.0.1:5000/api/courses/1) 
-H "Content-Type: application/json" 
-d '{
"status": "Completed"
}'

```

---

## Delete a Course

Endpoint

```

DELETE /api/courses/<id>

```

Example request:

```

curl -X DELETE [http://127.0.0.1:5000/api/courses/1](http://127.0.0.1:5000/api/courses/1)

```

---

# 6. Testing Instructions

You can test the API using command-line tools or API clients.

Recommended tools:

- curl
- Postman
- Thunder Client (VS Code extension)

Basic testing steps:

1. Start the Flask server
2. Use POST to add a course
3. Use GET to retrieve courses
4. Use PUT to update a course
5. Use DELETE to remove a course

Example test:

```

curl [http://127.0.0.1:5000/api/courses](http://127.0.0.1:5000/api/courses)

```

---

# 7. Troubleshooting Common Issues

Flask not installed

Error:

```

ModuleNotFoundError: No module named 'flask'

```

Solution:

```

pip install flask

```

---

Port already in use

Error:

```

Address already in use

```

Solution:

Stop other running applications using port 5000 or restart your terminal.

---

Invalid status value

Allowed values are:

```

Not Started
In Progress
Completed

```

---

JSON file issues

If the JSON file becomes corrupted, delete `courses.json` and restart the application. The file will be recreated automatically.

---

# 8. Project Structure Explanation

```

CodeCraftHub
│
├── app.py
├── courses.json
└── README.md

```

app.py

Main Flask application containing all REST API routes, validation logic, and file handling functions.

courses.json

Stores all course data in JSON format.

Example:

```

[
{
"id": 1,
"name": "Flask Basics",
"description": "Learn Flask",
"target_date": "2026-04-01",
"status": "In Progress",
"created_at": "2026-03-11T19:00:00"
}
]

```

README.md

Documentation file explaining how to install, run, test, and understand the project.
```
