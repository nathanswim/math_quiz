import sys
import htmlcreator 
from equation import Equation
from operation import Operation
from random import sample
from promptuser import PromptUser

"""print list of 12 times table"""

prompter = PromptUser()
prompter.test_yaml()

options = prompter.prompt()

LHS_LIST = list(range(options.lhs_min, options.lhs_max+1))
RHS_LIST = list(range(options.rhs_min, options.rhs_max+1))
OPERATION = options.operation
NUMBER_OF_QUESTIONS = options.number_of_questions

def ordered_question_list(lhs, rhs):
	"""take the lhs and rhs and produce an ordered list of questions"""
	result = []
	for l_n in lhs:
		for r_n in rhs:
			result.append(Equation(l_n, OPERATION, r_n))
	return result


def print_list(questions):
	"""Create html table"""
	for q_item in questions:
		print(q_item)
	return


question_list = ordered_question_list(LHS_LIST, RHS_LIST)

random_index = list(range(0,len(question_list)))
random_index = sample(random_index, len(random_index))

result = []

for i in range(0,NUMBER_OF_QUESTIONS):
	index = random_index[i%len(random_index)]
	question = question_list[index]
	result.append(question)

f = open("results.html", "w")
f.write(htmlcreator.create_html(result))
f.close()


