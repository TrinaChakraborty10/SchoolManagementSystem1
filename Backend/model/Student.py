class Student :
    def __init__(self, stud_id, name, dob, addr, class_id, school_id):
        self.stud_id = stud_id
        self.name = name
        self.dob = dob
        self.addr = addr
        self.class_id = class_id
        self.school_id = school_id

    def display_info(self):
        return f"{self.stud_id} {self.name} {self.dob} {self.addr} {self.class_id} {self.school_id}"