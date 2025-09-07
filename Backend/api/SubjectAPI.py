from dao import SubjectDao

@app.get("/subjects/")
def get_subjects(): 
    subjects = SubjectDao.getAllSubjects()
    return {"subjects": subjects}

@app.get("/subjects/{name}")
def get_subject_by_name(name: str):
    subject = SubjectDao.getSubjectByName(name)
    return {"subject": subject}

@app.post("/subjects/")
def create_subject(name: str, description: str):
    SubjectDao.insertSubject(name, description)
    return {"message": "Subject created successfully"}