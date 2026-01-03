from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create FastAPI app
app = FastAPI(title="Student Management API")

# Student Model
class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str

# Fake database
students: List[Student] = []

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}

# Create student
@app.post("/students", response_model=Student)
def create_student(student: Student):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")
    students.append(student)
    return student

# Get all students
@app.get("/students", response_model=List[Student])
def get_students():
    return students

# Get student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# Update student
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
