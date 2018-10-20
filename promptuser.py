import yaml
from operation import Operation
from useroptions import UserOptions

class PromptUser(object):
    def __init__(self):
        pass
    
    def test_yaml(self):
        stream = open("useroptions.yaml", "r")
        doc = yaml.load(stream)
        user_options = doc['user-options']

        #print user_options
        #print user_options[0]['name']
        #print user_options[1]['name']

        #     for k,v in doc:
        #         print k, "->", v
        #     print "\n"
        # 

    def get_names_from_yaml(self):
        stream = open("useroptions.yaml", "r")
        doc = yaml.load(stream)
        user_options = doc['user-options']
        result = []
        for option in user_options:
            result.append(option['name'])
        return result
    
    def getOptionsFromYaml(self, name):
        stream = open("useroptions.yaml", "r")
        doc = yaml.load(stream)
        user_options = doc['user-options']
        result = None
        for option in user_options:
            if option['name'] == name:
                result = UserOptions()
                result.operation = Operation.byNumber(option['operation'])
                result.lhs_min = option['lhs_min']
                result.lhs_max = option['lhs_max']
                result.rhs_min = option['rhs_min']
                result.rhs_max = option['rhs_max']
                result.number_of_questions = option['no_questions']
        return result
   


    def prompt(self):
        print("Which option do you want?")
        names = self.get_names_from_yaml()
        index = 0
        line_no = 1
        for i, name in enumerate(names):
            index = i
            line_no = index + 1
            print "  ", str(line_no) + ".", name
        index += 1
        line_no = index + 1
        print "  ", str(line_no) + ". Custom"

        option = input("Option number:")
        if option == line_no:
            return self.promptCustom()
        
        selected_name = names[option-1]
        result = self.getOptionsFromYaml(selected_name)
        if result == None:
            return self.promptCustom()
        return result


    def promptCustom(self):
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

