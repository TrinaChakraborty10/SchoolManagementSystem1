class School :
    def __init__(self, school_id, addr, board, coed, estd, medium, name) :
        self.school_id = school_id
        self.addr = addr
        self.board = board
        self.coed = coed
        self.estd = estd
        self.medium = medium 
        self.name = name

        def display_info(self):
            return f"{self.school_id} {self.addr} {self.board} {self.coed} {self.estd} {self.medium} {self.name}"