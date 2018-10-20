
class Operation(object):
    empty_instance = None

    def __init__(self, op):
        self.op = op
    def to_s(self):
        return self.op
    @staticmethod
    def byNumber(value):
        op_choices = {
            1: Operation.multiplication(),
            2: Operation.addition(),
            3: Operation.substraction(),
            4: Operation.division()
        }
        return op_choices.get(value, Operation.multiplication())
    @staticmethod
    def multiplication():
        return MultiplicationOperation()
    @staticmethod
    def division():
        return DivisionOperation()
    @staticmethod
    def addition():
        return AdditionOperation()
    @staticmethod
    def substraction():
        return SubtractionOperation()
    @staticmethod
    def empty():
        if not Operation.empty_instance:
            Operation.empty_instance = EmptyOperation()
        return Operation.empty_instance

class MultiplicationOperation(Operation):
    def __init__(self):
        super(MultiplicationOperation, self).__init__("x")

class DivisionOperation(Operation):
    def __init__(self):
        super(DivisionOperation, self).__init__("÷")

class AdditionOperation(Operation):
    def __init__(self):
        super(AdditionOperation, self).__init__("+")

class SubtractionOperation(Operation):
    def __init__(self):
        super(SubtractionOperation, self).__init__("-")

class EmptyOperation(Operation):
    def __init__(self):
        super(EmptyOperation, self).__init__("")


