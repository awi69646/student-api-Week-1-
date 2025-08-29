from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    program: str

students: List[Student] = []

@app.get("/students", response_model=List[Student])
def get_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students", response_model=Student)
def add_student(student: Student):
    students.append(student)
    return student

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return {"message": f"Student {student_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
