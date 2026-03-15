from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 


app = FastAPI()

students = {
    1: {"name": "Alice", "age": 20},
    2: {"name": "Bob", "age": 22},
    3: {"name": "Charlie", "age": 21}
}

class Student(BaseModel):
    name: str
    age: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


@app.get("/")
def read_jokes():
    return {"joke": "Why did the scarecrow win an award? Because he was outstanding in his field!"}

@app.post("/jokes")
def create_joke(joke: str):
    
    return {'message': f'Joke received: {joke}'}

@app.get('/get-joke-name')
def get_joke_name( *, name: Optional [str] = None):
    
    for student in students:
        if students[student]['name'] == name:
            return students[student]
    return {"error": "Student not found"} 

@app.post('/add-student/{student_id}')
def create_student(student_id: int, student: Student):
    
    if student_id in students:
        return {"error": "Student ID already exists"}
    
    students[student_id] = student.model_dump()
    return {"message": "Student added successfully", "student_id": student_id, 'student': students[student_id]}

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"error": "Student not found"}
    if student.name != None: 
        students[student_id]['name'] = student.name
        
    if student.age != None: 
        students[student_id]['age'] = student.age
    return {'message': 'student updated successfully', 'student':students[student_id]}
    
@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    
    del students[student_id]
    return {"message": "Student deleted successfully"}
    