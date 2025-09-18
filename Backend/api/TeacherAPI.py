from fastapi import FastAPI
from dao import TeacherDao
from fastapi import APIRouter

router = APIRouter()   

@router.get("/teachers/")
def get_teachers():
    teachers = TeacherDao.getAllTeachers()
    return {"teachers": teachers}

@router.get("/teachers/{name}")
def get_teacher_by_name(name: str):
    teacher = TeacherDao.getTeacherbyName(name)
    return {"teacher": teacher}

@router.post("/teachers/")
def create_teacher(name: str, subject: str):
    TeacherDao.insertTeacher(name, subject)
    return {"message": "Teacher created successfully"}