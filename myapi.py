from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


students = {
    1: {
        "Name": "John",
        "Age": 18,
        "Class": "Grade 12"
    }
}

class Student(BaseModel):
    Name: str
    Age: int
    Class: str

@app.get("/")
def index():
    return {"Name": "First Message"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="Enter the Id of the student that you want to view", gt=0, lt=3)):
    return students[student_id]


@app.get("/get-student-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str]= None, test: int):
    for student_id in students:
        if students[student_id]["Name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}


@app.post("/create-new-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Already Exists"}
    
    students[student_id] = student
    return students[student_id]