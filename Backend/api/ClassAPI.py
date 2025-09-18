from fastapi import FastAPI
from dao import ClassDao
from fastapi import APIRouter

router = APIRouter()

@router.get("/classes/")
def get_classes():
    classes = ClassDao.getAllClass()
    return {"classes": classes}

@router.get("/classes/{name}")
def get_class_by_name(name: str):
    class_ = ClassDao.getClassbyName(name)
    return {"class": class_}

@router.post("/classes/")
def create_class(name: str):
    ClassDao.insertClass(name)
    return {"message": "Class created successfully"}
