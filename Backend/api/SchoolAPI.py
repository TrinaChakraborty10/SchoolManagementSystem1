from dao import SchoolDao

@app.get("/schools/")
def get_schools():
    schools = SchoolDao.getAllSchool()
    return {"schools": schools}

@app.get("/schools/{name}")
def get_school_by_name(name: str):
    school = SchoolDao.getSchoolbyName(name)
    return {"school": school}

@app.post("/schools/")
def create_school(name: str, address: str):
    SchoolDao.insertSchool(name, address)
    return {"message": "School created successfully"}