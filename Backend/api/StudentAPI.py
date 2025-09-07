from fastapi import FastAPI
from dao import StudentDao
from fastapi import APIRouter

router = APIRouter()

@router.get("/students/")
def get_students():
    students = StudentDao.getAllStudents()
    return {"students": students}

@router.get("/students/{name}")
def get_student_by_name(name: str):
    student = StudentDao.getStudentByName(name)
    return {"student": student}

@router.post("/students/")
def create_student(name: str, age: int, address: str):
    StudentDao.insertStudent(name, age, address)
    return {"message": "Student created successfully"}

