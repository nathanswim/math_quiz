from operation import Operation
class Equation(object):
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    def LHS(self):
        return str(self.lhs)
    def Operation(self):
        return self.op
    def RHS(self):
        return str(self.rhs)
    def to_s(self):
        return str(self.lhs) + ' ' + self.op.to_s() + ' ' + str(self.rhs) + ' = '
