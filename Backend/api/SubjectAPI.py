from fastapi import FastAPI
from dao import SubjectDao
from fastapi import APIRouter

router = APIRouter()

@router.get("/subjects/")
def get_subjects(): 
    subjects = SubjectDao.getAllSubject()
    return {"subjects": subjects}

@router.get("/subjects/{name}")
def get_subject_by_name(name: str):
    subject = SubjectDao.getSubjectbyName(name)
    return {"subject": subject}

@router.post("/subjects/")
def create_subject(name: str):
    SubjectDao.insertSubject(name)
    return {"message": "Subject created successfully"}