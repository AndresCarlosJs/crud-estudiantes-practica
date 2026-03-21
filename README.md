# Simple Student CRUD API

A simple RESTful API built with **FastAPI** to manage student records.  
This project demonstrates basic **CRUD operations** (Create, Read, Update, Delete) using an **in-memory database**.

---

## 🛠 Features

- ✅ Retrieve a list of students or a single student by ID
- ✅ Retrieve a student by name
- ✅ Add a new student
- ✅ Update an existing student (partial update supported)
- ✅ Delete a student
- 📦 Built with **FastAPI** and **Pydantic**
- 🏗 In-memory storage (dictionary) — no external database required

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/MissaouiYassine1/simple-student-crud.git
cd simple-student-crud
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install fastapi uvicorn
```
## 🚀 Running the API

Start the server with uvicorn:
```bash
uvicorn main:app --reload
```
main → the Python file name (main.py)

--reload → enables auto-reload during development

The API will be accessible at:

##### http://127.0.0.1:8000
## 📚 API Endpoints
#### Method	Endpoint	Description
##### GET	/	Root endpoint for testing
##### GET	/get-students/{student_id}	Retrieve a student by ID
##### GET	/get-by-name/{student_id}?name=<name>&test=<value>	Retrieve a student by name
##### POST	/create-student/{student_id}	Create a new student
##### PUT	/update-student/{student_id}	Update an existing student (partial update allowed)
##### DELETE	/delete-student/{student_id}	Delete a student by ID
## 📝 Data Model
###### Student (Create)
{
  "name": "John",
  "age": 20,
  "class_name": "A"
}
###### UpdateStudent (Update)

###### All fields optional:

{
  "name": "John Doe",
  "age": 21,
  "class_name": "B"
}
## 🔧 Notes

- Currently, the API uses an in-memory dictionary.
- All data will be lost when the server restarts.

- For production, connect it to a proper database like PostgreSQL, MySQL, or MongoDB.

- __pycache__ and virtual environment folders should be ignored in .gitignore.

## 🖼 Testing & Docs

FastAPI provides interactive documentation:

##### - Swagger UI: http://127.0.0.1:8000/docs

##### - ReDoc: http://127.0.0.1:8000/redoc

#### You can test all endpoints directly from your browser.

## 👨‍💻 Author

### Yassine Missaoui
### GitHub: MissaouiYassine1
