from dao import TeacherDao

@app.get("/teachers/")
def get_teachers():
    teachers = TeacherDao.getAllTeachers()
    return {"teachers": teachers}

@app.get("/teachers/{name}")
def get_teacher_by_name(name: str):
    teacher = TeacherDao.getTeacherByName(name)
    return {"teacher": teacher}

@app.post("/teachers/")
def create_teacher(name: str, subject: str):
    TeacherDao.insertTeacher(name, subject)
    return {"message": "Teacher created successfully"}