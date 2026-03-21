# import the FastAPI framework to build APIs
from typing import Optional

from fastapi import FastAPI, Path

# import Pydantic to define request/response data models with validation
from pydantic import BaseModel

# create an instance of the FastAPI application
app = FastAPI()

# in-memory database (dictionary) to store student data
# key = student_id, value = student information
students = {
    1: {"name": "John", "age": 20, "class": "A"},
    2: {"name": "Jane", "age": 22, "class": "B"},
    3: {"name": "Doe", "age": 21, "class": "C"}
}

# data model for creating a new student (request body)
# all fields are required
class Student(BaseModel):
    name: str          # student's name
    age: int           # student's age
    class_name: str    # student's class (renamed to avoid conflict with Python keyword "class")

# data model for updating a student
# all fields are optional (partial update allowed)
class UpdateStudent(BaseModel):
    name: Optional[str] = None        # optional name update
    age: Optional[int] = None         # optional age update
    class_name: Optional[str] = None  # optional class update

# root endpoint (basic test route)
@app.get("/")
def index():
    return {
        "message": "I'm the root"
    }

# endpoint to retrieve a student by ID
@app.get("/get-students/{student_id}")
def get_students(
    student_id: int = Path(
        ..., 
        description="The ID of the student to retrieve\n",
        gt=0,  # must be greater than 0
        lt=students.__len__() + 1  # must be less than number of students + 1
    )
):
    # search for student in the dictionary
    student = students.get(student_id)

    # if student not found, return error
    if not student:
        return {"error": "Student not found"}

    # return student data
    return student

# endpoint to retrieve a student by name (query parameter)
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    # loop through all students
    for student_id in students:
        # check if name matches
        if students[student_id]["name"] == name:
            return students[student_id]

    # if no match found
    return {"error": "Student not found"}

# endpoint to create a new student
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    # check if student ID already exists
    if student_id in students:
        return {"error": "Student ID already exists"}

    # add new student to dictionary
    students[student_id] = student.dict()

    # return created student
    return students[student_id]

# endpoint to update an existing student
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    # check if student exists
    if student_id not in students:
        return {"error": "Student doesn't exists"}

    # update only provided fields (partial update logic)
    if student.name is not None:
        students[student_id]["name"] = student.name

    if student.age is not None:
        students[student_id]["age"] = student.age

    if student.class_name is not None:
        students[student_id]["class_name"] = student.class_name

    students[student_id] = student

    # return updated student
    return students[student_id]