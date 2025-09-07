class Teacher :
    def __init__(self, tch_id, name, subject, teaching_experience, school_id):
        self.teacher_id = tch_id
        self.name = name
        self.subject = subject
        self.teaching_experience = teaching_experience
        self.school_id = school_id

    def display_info(self):
        return f"{self.teacher_id} {self.name} {self.subject} {self.teaching_experience} {self.school_id}"