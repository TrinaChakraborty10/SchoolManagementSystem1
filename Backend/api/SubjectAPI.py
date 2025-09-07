from fastapi import FastAPI
from dao import SubjectDao
from fastapi import APIRouter

router = APIRouter()

@router.get("/subjects/")
def get_subjects(): 
    subjects = SubjectDao.getAllSubjects()
    return {"subjects": subjects}

@router.get("/subjects/{name}")
def get_subject_by_name(name: str):
    subject = SubjectDao.getSubjectByName(name)
    return {"subject": subject}

@router.post("/subjects/")
def create_subject(name: str, description: str):
    SubjectDao.insertSubject(name, description)
    return {"message": "Subject created successfully"}