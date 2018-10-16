from operation import Operation
class Equation(object):
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    def LHS(self):
        return self.lhs
    def Operation(self):
        return self.op
    def RHS(self):
        return self.rhs
    def to_s(self):
        ops = {
            Operation.Addition: "+",
            Operation.Subtraction: "-",
            Operation.Muliplication: "x",
            Operation.Division: "÷"
        }
        op = ops.get(self.op, "?")
        return str(self.lhs) + ' ' + op + ' ' + str(self.rhs) + ' = '
