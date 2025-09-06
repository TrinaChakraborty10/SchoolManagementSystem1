class School :
    def __init__(self, sub_id, sub_name):
        self.sub_id = sub_id
        self.sub_name = sub_name

    def display_info(self):
        return f"{self.sub_id} {self.sub_name}"