import sys
from htmlcreator import *
from equation import Equation
from operation import Operation
from random import sample

"""print list of 12 times table"""

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


LHS_LIST = list(range(LHS_START, LHS_END+1))
RHS_LIST = list(range(RHS_START, RHS_END+1))

def ordered_question_list(lhs, rhs):
	"""take the lhs and rhs and produce an ordered list of questions"""
	result = []
	for l_n in lhs:
		for r_n in rhs:
			result.append(Equation(l_n, Operation.Muliplication, r_n))
	return result


def print_list(questions):
	"""Create html table"""
	for q_item in questions:
		print(q_item)
	return


question_list = ordered_question_list(LHS_LIST, RHS_LIST)
print(question_list)

random_index = list(range(0,len(question_list)))
print(random_index)
random_index = sample(random_index, len(random_index))
print(random_index)

result = []

for i in range(0,NUMBER_OF_QUESTIONS):
	index = random_index[i%len(random_index)]
	print(index)
	question = question_list[index]
	result.append(question)




f = open("results.html", "w")
f.write(create_html(result))
f.close()


