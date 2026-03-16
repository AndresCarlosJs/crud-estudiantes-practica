#import the fastapi library
from fastapi import FastAPI,Path

#create an instance of the fastapi class
app = FastAPI()

# create a dictionary to store student data
students = {
    1: {"name": "John", "age": 20, "class": "A"},
    2: {"name": "Jane", "age": 22, "class": "B"},
    3: {"name": "Doe", "age": 21, "class": "C"}
}
# define a route for the root endpoint
@app.get("/")
def index():
    return {
        "message":"I'm the root"
    }

@app.get("/get-students/{student_id}")
def get_students(student_id: int = Path(..., description="The ID of the student to retrieve\n", gt=0, lt=students.__len__() + 1)):
    student = students.get(student_id)
    if not student:
        return {"error": "Student not found"}
    return student