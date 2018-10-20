from operation import Operation

class UserOptions(object):
    def __init__(self):
        self.lhs_min = 1
        self.lhs_max = 12
        self.rhs_min = 1
        self.rhs_max = 12
        self.operation = Operation.multiplication()
        self.number_of_questions = 100
    
