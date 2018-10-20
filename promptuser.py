import yaml
from operation import Operation
from useroptions import UserOptions

class PromptUser(object):
    def __init__(self):
        pass
    def prompt(self):
        print("Which operation do you want?")
        print("  1. Multiplication")
        print("  2. Addition")
        print("  3. Subtraction")
        print("  4. Division")

        text = input("Operation: ")
        op_choice = int(text)
        op_choices = {
            1: Operation.multiplication(),
            2: Operation.addition(),
            3: Operation.substraction(),
            4: Operation.division()
        }

        OPERATION = op_choices.get(op_choice, Operation.multiplication())
#
        text = input("Left hand side start: ")
        LHS_START = int(text)

        text = input("Left hand side end: ")
        LHS_END = int(text)

        text = input("Right hand side end: ")
        RHS_START = int(text)

        text = input("Right hand side end: ")
        RHS_END = int(text)

        text = input("Number of questions: ")
        NUMBER_OF_QUESTIONS = int(text)

        result = UserOptions()
        result.operation = OPERATION
        result.lhs_min = LHS_START
        result.lhs_max = LHS_END
        result.rhs_min = RHS_START
        result.rhs_max = RHS_END
        result.number_of_questions = NUMBER_OF_QUESTIONS
        return result

    def test_yaml(self):
        stream = open("useroptions.yaml", "r")
        doc = yaml.load(stream)
        for item in doc.items:
            print item
        #     for k,v in doc:
        #         print k, "->", v
        #     print "\n"