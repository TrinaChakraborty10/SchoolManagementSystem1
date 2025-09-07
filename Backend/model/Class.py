class Class :
    def __init__(self, class_id, class_name, school) :
        self.class_id = class_id
        self.class_name = class_name
        self.school = school

        def display_info(self):
            return f"{self.class_id} {self.class_name} {self.school}"