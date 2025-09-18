from fastapi import FastAPI
from dao import SchoolDao
from fastapi import APIRouter

router = APIRouter()

@router.get("/schools/")
def get_schools():
    schools = SchoolDao.getAllSchool()
    return {"schools": schools}

@router.get("/schools/{name}")
def get_school_by_name(name: str):
    school = SchoolDao.getSchoolbyName(name)
    return {"school": school}

@router.post("/schools/")
def create_school(address: str, board: str, coed: str, estd: str, medium: str, name: str):
    SchoolDao.insertSchool(address, board, coed, estd, medium, name)
    return {"message": "School created successfully"}