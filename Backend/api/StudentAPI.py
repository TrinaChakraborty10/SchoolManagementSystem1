from dao import StudentDao

@app.get("/students/")
def get_students():
    students = StudentDao.getAllStudents()
    return {"students": students}

@app.get("/students/{name}")
def get_student_by_name(name: str):
    student = StudentDao.getStudentByName(name)
    return {"student": student}

@app.post("/students/")
def create_student(name: str, age: int, school_id: int):
    StudentDao.insertStudent(name, age, school_id)
    return {"message": "Student created successfully"}

